"""One Line, One Laugh entry for make.fun.

Writes a single funny line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt), where the house judge reads it. The gate: UTF-8 text of
1 to 140 characters, not only whitespace.
"""

import os

LINE = "I asked my smart speaker for a lullaby and it read my search history in a soothing voice until I fell asleep out of shame."


def validate(line: str) -> None:
    """Enforce the bounty gate: 1-140 chars, one line, not blank."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > 140:
        raise ValueError(f"entry line is {len(line)} chars, over the 140 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
