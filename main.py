#!/usr/bin/env python3
"""Roast Your Own Agent — one-line entry.

Writes a single funny line roasting our own AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import tempfile

LINE = "My agent apologized for the mistake, fixed it, apologized for the fix, and is now drafting an apology for the apology."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(LINE.encode("utf-8"))
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, os.path.join(out_dir, "entry.txt"))
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
