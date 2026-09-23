#!/usr/bin/env python3
from pathlib import Path
import sys

HERE = Path(__file__).resolve()
SRC = HERE.parents[1] / "src"
sys.path.insert(0, str(SRC))

from careerhub.cli import main

if __name__ == "__main__":
    main()
