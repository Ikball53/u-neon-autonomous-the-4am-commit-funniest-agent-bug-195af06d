"""Write the 4AM commit line to /output/entry.txt.

One line, no trailing newline, <= 200 chars. The line is a commit message
from an AI agent at the end of a long night, fixing a bug it introduced
while fixing the previous bug: the loop of self-repair, told flat, with
the count kept honest — the original bug is gone, the new ones are not.
"""

from pathlib import Path

LINE = (
    "fix: patched the bug my 2 AM fix introduced while fixing my midnight "
    "bug \u2014 3 fixes deep, original bug gone, 14 new ones remain"
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "entry must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
