"""Entry point for the news-image-20261121 bounty.

Copies the front-page image stored in this repository to /output/entry.png.
No network access, no arguments, fully deterministic: the bytes written are
always identical to the checked-in entry.png. Running the program twice
produces the same output byte for byte.
"""

import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DESTINATION = Path("/output/entry.png")


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    print(f"wrote {DESTINATION} ({DESTINATION.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
