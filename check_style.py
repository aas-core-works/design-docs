import pathlib
import os
import re
import sys
from typing import List

LINK_DEFINITION_RE = re.compile(r'^\s*\[[^]]+\]\s*:')


def check(path: pathlib.Path) -> List[str]:
    """Check that the document conforms to the style guide."""
    errors = []  # type: List[str]

    lines = path.read_text().splitlines()

    for i, line in enumerate(lines):
        if LINK_DEFINITION_RE.match(line):
            continue

        if len(line) > 88:
            errors.append(
                f"The line {i + 1} is too long. Expected at most 88 characters, "
                f"got: {len(line)}")

    return errors


def main() -> int:
    docs_dir = pathlib.Path(os.path.realpath(__file__)).parent / "docs"
    for pth in sorted(docs_dir.glob("**/*.md")):
        errors = check(path=pth)

        if errors:
            print(f"There were style errors in: {pth}", file=sys.stderr)
            for error in errors:
                print(f"* {error}", file=sys.stderr)

            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
