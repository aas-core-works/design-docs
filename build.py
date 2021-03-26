"""Render the design docs into HTML."""
import argparse
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o", "--output", help="Output directory where HTML will reside",
        default="html")
    args = parser.parse_args()

    output_dir = str(args.output)

    run = subprocess.run(['mkdocs', '--version'])
    if run.returncode != 0:
        print(
            "The `mkdocs` has not been installed. "
            "Have you installed it on your system or your virtual environment?",
            file=sys.stderr)
        return 1

    print("Building the site with mkdocs...")
    subprocess.check_call(['mkdocs', 'build', '--strict', '--site-dir', output_dir])

    print()
    print("You can serve the website with: mkdocs serve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
