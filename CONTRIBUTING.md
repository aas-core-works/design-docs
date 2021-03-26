# Contributing

We use [mkdocs] to render the design documentation.

[mkdocs]: https://www.mkdocs.org/

## Setting up the Environment

To set up the evnironment for building the documentation, change to the
root folder of the repository and execute:

```
python -m venv venv
```

This will create the directory `venv/` containing your virtual environment.

To activate it, run in Windows:

```
venv\Scripts\activate
```

or in Linux/OS X:

```
source venv/bin/activate
```

## Installing mkdocs

In your activated virtual environment, run `pip` to install [mkdocs] and 
other dependencies:

```
pip install -r requirements.txt 
```

## Building the Documentation

The documentation is built using `build.py` script:

```
python build.py
```

By default, the generated files will reside in `html/` directory.
You can change the output directory with `--output`:

```
python build.py --output some/other/directory
```

## Checking the Markdown Style

We enforce a minimal set of style rules on our markdown files (*e.g.*, maximum line 
width of 88 characters).

To check the style, run:

```
python check_style.py
```

## Commit Messages

The commit messages follow the guidelines from
https://chris.beams.io/posts/git-commit:

* Separate subject from body with a blank line
* Limit the subject line to 50 characters
* Capitalize the subject line
* Do not end the subject line with a period
* Use the imperative mood in the subject line
* Wrap the body at 72 characters
* Use the body to explain *what* and *why* (instead of *how*)

We automatically check the commit messages using [opinionated-commit-message].

[opinionated-commit-message]: https://github.com/mristin/opinionated-commit-message
