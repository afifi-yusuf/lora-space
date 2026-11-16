# Contributing

## Reporting a problem with a result

Every score on [loraspace.org](https://loraspace.org) links to its run, and every run's record is in
[`results/lsbench/runs/`](results/lsbench/runs/). If a result looks wrong, open an issue that names the run directory
and says what you expected. The most useful reports point at a line in `result.json`, `session.json` or
`tool_calls.jsonl`.

## Proposing an editor, a harness or a task

Open an issue first. Runs are made on the maintainers' GPU hosts so that every entry gets the same hardware, limits
and rules version, so a new entry is something we schedule, not something a pull request can add on its own.

- **An editor or harness** needs an entry in [`lsbench/config/entries.toml`](lsbench/config/entries.toml) and, for a
  new harness, an Agency adapter.
- **A task** needs a request, a held-out set the editor never sees, the unedited model's score on it, and at least one
  reference score to define 100 on the scale. See the files in [`lsbench/config/tasks/`](lsbench/config/tasks/).

## Changing the code

```bash
uvx --with numpy pytest -q     # unit tests
python3 -m lsbench.site        # rebuilds site/index.html from the run records; needs no GPU
```

- Lines are at most 110 characters (`[tool.ruff]` in `pyproject.toml`).
- Anything that changes what an editor sees or is allowed to do (the task text, a tool, a limit) changes the settings
  hash, and results made before and after are no longer ranked together. Bump `RULES_VERSION` in `lsbench/spec.py`
  and say so in the pull request.
- Never commit credentials. `secrets.env` and service-account files are git-ignored; keep them that way.
