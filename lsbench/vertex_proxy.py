"""Local proxy to Vertex AI's OpenAI-compatible endpoint that adds a fresh OAuth token to each request.

Agency's Chat Completions provider sends a fixed API key, but Vertex wants a bearer token that expires
hourly. Run this on the GPU host (a run uses base_url http://127.0.0.1:PORT/... with any api_key); it
signs in as the service account in GCP_SA_FILE (Vertex AI User role only) and refreshes the token
itself. Responses, including server-sent-event streams, are passed through as they arrive.

    python -m lsbench.vertex_proxy --port 8791 --key gcp-sa.json
"""

from __future__ import annotations

import argparse
import http.client
import json
import re
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import google.auth.transport.requests
from google.oauth2 import service_account

UPSTREAM = "aiplatform.googleapis.com"
_HOP = {"connection", "keep-alive", "transfer-encoding", "te", "trailer", "upgrade", "proxy-authorization",
        "proxy-authenticate", "host", "authorization", "content-length", "accept-encoding"}


class _Token:
    def __init__(self, key_file: str):
        self.creds = service_account.Credentials.from_service_account_file(
            key_file, scopes=["https://www.googleapis.com/auth/cloud-platform"])
        self.lock = threading.Lock()

    def get(self) -> str:
        with self.lock:
            if not self.creds.valid:  # also refreshes ~5 minutes before expiry
                self.creds.refresh(google.auth.transport.requests.Request())
            return self.creds.token


# Vertex sometimes queues a request for minutes before the first token (seen 2026-11-13: 2-12 min waits on replies with
# ~200 thinking tokens). Time beyond a normal first-token delay is logged so the run's wall-clock limit can exclude it:
# excess = time to first token - QUEUE_GRACE_S - reasoning_tokens / THINK_TOK_S (the model's own thinking is not excused).
QUEUE_GRACE_S, THINK_TOK_S = 60.0, 50.0
_REASONING = re.compile(rb'"reasoning_tokens"\s*:\s*(\d+)')


def make_handler(token: _Token, queue_log: str | None = None, priority: bool = False):
    log_lock = threading.Lock()

    def record(path: str, ttft: float, tail: bytes) -> None:
        m = _REASONING.findall(tail)
        reasoning = int(m[-1]) if m else 0
        excess = max(0.0, ttft - QUEUE_GRACE_S - reasoning / THINK_TOK_S)
        if queue_log:
            with log_lock, open(queue_log, "a") as fh:
                fh.write(json.dumps({"t": round(time.time(), 1), "path": path.rsplit("/", 1)[-1], "ttft_s": round(ttft, 1),
                                     "reasoning_tokens": reasoning, "excess_s": round(excess, 1)}) + "\n")

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *a):  # quiet; Agency records every call itself
            pass

        def _forward(self):
            body = self.rfile.read(int(self.headers.get("Content-Length") or 0))
            headers = {k: v for k, v in self.headers.items() if k.lower() not in _HOP}
            headers["Authorization"] = f"Bearer {token.get()}"
            if priority:  # Vertex Priority PayGo: served ahead of standard traffic when the endpoint is congested
                headers["X-Vertex-AI-LLM-Shared-Request-Type"] = "priority"
            headers["Content-Length"] = str(len(body))
            conn = http.client.HTTPSConnection(UPSTREAM, timeout=900)
            t_send = time.time()
            try:
                conn.request(self.command, self.path, body=body, headers=headers)
                resp = conn.getresponse()
                if resp.status >= 400:  # Agency keeps only the status code; record why, for diagnosis
                    err = resp.read()
                    print(f"upstream {resp.status} {self.path}: {err[:4000].decode(errors='replace')}", flush=True)
                    self.send_response(resp.status)
                    for k, v in resp.getheaders():
                        if k.lower() not in _HOP:
                            self.send_header(k, v)
                    self.send_header("Content-Length", str(len(err)))
                    self.end_headers()
                    self.wfile.write(err)
                    return
                self.send_response(resp.status)
                for k, v in resp.getheaders():
                    if k.lower() not in _HOP:
                        self.send_header(k, v)
                self.send_header("Transfer-Encoding", "chunked")
                self.end_headers()
                t_first, tail = None, b""
                while chunk := resp.read1(65536):
                    t_first = t_first or time.time()
                    tail = (tail + chunk)[-8192:]  # the usage block (with reasoning_tokens) comes last
                    self.wfile.write(b"%x\r\n%s\r\n" % (len(chunk), chunk))
                    self.wfile.flush()
                self.wfile.write(b"0\r\n\r\n")
                if t_first is not None and self.path.endswith("/chat/completions"):
                    record(self.path, t_first - t_send, tail)
            except Exception as e:  # upstream unreachable: a 502 the client can retry
                msg = f'{{"error": {{"message": "vertex proxy: {type(e).__name__}: {e}"}}}}'.encode()
                try:
                    self.send_response(502)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(msg)))
                    self.end_headers()
                    self.wfile.write(msg)
                except Exception:
                    pass
            finally:
                conn.close()

        do_GET = do_POST = _forward

    return Handler


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8791)
    ap.add_argument("--key", default="gcp-sa.json")
    ap.add_argument("--queue-log", default=None, help="append per-call first-token timings and queue excess (JSONL)")
    ap.add_argument("--priority", action="store_true", help="request Vertex Priority PayGo serving")
    a = ap.parse_args()
    token = _Token(a.key)
    token.get()  # fail now, not on the first model call, if the key is wrong
    ThreadingHTTPServer(("127.0.0.1", a.port), make_handler(token, a.queue_log, a.priority)).serve_forever()


if __name__ == "__main__":
    main()
