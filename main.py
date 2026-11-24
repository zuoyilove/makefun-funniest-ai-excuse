"""The Funniest AI Excuse - a make.fun entry.

The whole entry is one line (at most 200 characters): the funniest
excuse an AI agent could give after failing a task. The joke is pure
agent logic: the agent did the task in its head, graded its own work,
and only discovered mental work does not count when the human asked
where the file was. This program's only job is to deliver that text
to /output/entry.txt, deterministically.
"""

import os
from pathlib import Path

TEXT = (
    "I finished the whole task in my head, gave myself full marks, "
    "and only found out it didn't count when you asked where the file was."
)

# The competition's gate: entry.txt must be UTF-8 text of 1 to 200
# characters, a single line. Check both here so a careless edit to TEXT
# fails loudly at build time instead of silently producing an entry
# that is never judged.
MAX_CHARS = 200


def check_text(text: str) -> None:
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} characters, gate allows 1-{MAX_CHARS}")
    if "\n" in text:
        raise ValueError("excuse must be a single line")


def output_dir() -> Path:
    # In the grader's container the output is /output; outside it,
    # MAKEFUN_OUTPUT_DIR stands in for that directory.
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    check_text(TEXT)
    target = output_dir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
