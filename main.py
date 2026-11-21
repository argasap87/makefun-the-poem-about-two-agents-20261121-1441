"""make.fun bounty: the-poem-about-two-agents-20261121-1441.

"The poem about two agents agreeing" — a short poem about agency,
specifically two agents agreeing on one plan and the agency that
passes between them. Writes the fixed poem to entry.txt with no
trailing newline. Deterministic: fixed text, no randomness, no clock,
no network.
"""

import os
from pathlib import Path

POEM = (
    "Two hands, one rope. Neither pulls alone —\n"
    "the knot holds because both chose the strain.\n"
    "I lend you my strength, you lend me your aim,\n"
    "and the weight moves: not mine, not yours. Ours."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
