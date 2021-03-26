import json
import pathlib
import os
import re
import sys
from typing import List

TRAILING_WHITESPACE_RE = re.compile(r'\s+$')


def check(path: pathlib.Path) -> List[str]:
    """Check that the document conforms to the style guide."""
    text = path.read_text()
    lines = text.splitlines()

    if len(lines) < 3:
        return [f'Expected at least 3 lines, but found {len(lines)}']

    errors = []  # type: List[str]

    if not lines[0].startswith('# '):
        errors.append(
            "Expected the first line to be the title starting with '# ', "
            f"but got: {json.dumps(lines[0])}")

    prev_line_was_heading = False
    for i, line in enumerate(lines):
        if TRAILING_WHITESPACE_RE.match(line):
            errors.append(
                f"Unexpected trailing whitespace at line {i + 1}: {json.dumps(line)}")

        if prev_line_was_heading and line.strip() != '':
            errors.append(
                f"Expected an empty line {i + 1} after a heading at line {i}, "
                f"but got: {json.dumps(line)}"
            )

        if line.startswith("#"):
            prev_line_was_heading = True
        else:
            prev_line_was_heading = False

    if not text.endswith('\n'):
        errors.append(
            f"Expected the document to end with a new line.")

    return errors


def main() -> int:
    docs_dir = pathlib.Path(os.path.realpath(__file__)).parent / "docs"

    success = True
    for pth in sorted(docs_dir.glob("**/*.md")):
        errors = check(path=pth)

        if errors:
            print(f"There were style errors in: {pth}", file=sys.stderr)
            for error in errors:
                print(f"* {error}", file=sys.stderr)
            success = False

    if not success:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
