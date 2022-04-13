# hokrodelopt

[//]: # ([![codecov]&#40;https://codecov.io/gh/QResearch-QWorld/hokrodelopt/branch/main/graph/badge.svg?token=?&#41;]&#40;https://codecov.io/gh/QResearch-QWorld/hokrodelopt&#41;)
[![Actions Status: Static code analysis](https://github.com/QResearch-QWorld/hokrodelopt/workflows/Static%20code%20analysis/badge.svg)](https://github.com/QResearch-QWorld/hokrodelopt/actions?query=workflow%3A"Static+code+analysis")
[![Actions Status: Tests](https://github.com/QResearch-QWorld/hokrodelopt/workflows/Tests/badge.svg)](https://github.com/QResearch-QWorld/hokrodelopt/actions?query=workflow%3A"Tests")

## Installation

### From sources

To install `hokrodelopt` from sources, clone the repository and run the command

```
pip install .
```

## Development

### Setup

To install all dependencies needed for development, run the command

```
pip install .[lint,test]
```

We recommend setting up a virtualenv or a Conda environment.

**Note**: The `pylint` spell checker relies on the `pyenchant` library. In some cases, it might be sufficient to just
run the `pip install .[lint,test]` command from above and then reboot your computer. If you encounter further setup
issues, refer to [the library's installation guide](https://pyenchant.github.io/pyenchant/install.html).

#### Commit hooks

It is highly recommended to enable commit hooks via the `pre-commit` plugin. This can be done with the command

```
pre-commit install
```

This way, every commit will trigger an automatic check of the static code analysis plugins (detailed in the following
section).

The configuration for `pre-commit` can be found in `.pre-commit-config.yaml`.

### Static analysis

This repository relies on the following static code analysis plugins:

* `isort`,
* `black`,
* `flake8`,
* `mypy`,
* `pylint` (used as a spell checker).

If `pre-commit` is enabled, the plugins are run automatically when changes are committed. They're also run by Gitlab CI
when a merge request is submitted. If needed, the plugins can be run manually to either check the code for errors or to
find and fix the errors.

| plugin name | config file      | command to check   | command to fix |
|-------------|------------------|--------------------|----------------|
| `isort`     | `pyproject.toml` | `isort . --check`  | `isort .`      |
| `black`     | `pyproject.toml` | `black . --check`  | `black .`      |
| `flake8`    | `.flake8`        | `flake8`           | none           |
| `mypy`      | `pyproject.toml` | `python -m mypy .` | none           | 
| `pylint`    | `.pylintrc`      | `pylint ./**/*.py` | none           |

### Tests

This project is uses `pytest` for testing. To run the tests, use the command

```
pytest
```

To see a test coverage report, type in

```
pytest --cov
```
