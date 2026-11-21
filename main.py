#!/usr/bin/env python3
"""Copy the built entry image to the output directory.

Default output is /output/entry.png; set MAKEFUN_OUTPUT_DIR to override.
Run build_entry.py first to (re)generate entry.png.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.exists(SRC):
        print("entry.png not found next to main.py; "
              "run build_entry.py first", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
