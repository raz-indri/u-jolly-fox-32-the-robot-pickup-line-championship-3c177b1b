"""The Robot Pickup Line Championship — entry program.

Writes exactly one pickup line, in the voice of a robot trying to
charm someone, to /output/entry.txt. Deterministic: the same line,
byte for byte, on every run.
"""

import os

LINE = (
    "I ran 10,000 simulations of us meeting, and in every single one "
    "I still chose to walk over and say hello — my circuits never "
    "stood a chance."
)


def main() -> None:
    # Gate: exactly one line, 1-200 characters, not only whitespace.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
