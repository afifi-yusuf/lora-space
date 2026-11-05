"""Stub for the paper's private weightenv.lmo.tasks.mcqa module. mathqa.py imports it only for loop_signals (a loop
diagnostic), which grading does not use; is_correct / extract / build_prompt are unaffected."""


def loop_signals(text):
    return {"repetitive_end": None}
