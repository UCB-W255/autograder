# MIDS 255 Autograding

This repo represents the autograding for UC Berkeley's MIDS 255 class.

We currently have this repository public to support students while we develop the test cases. This will likely be made a private repo over time.

## Why?

MIDS 255 is a very intensive class that requires signfiicant effort from students. The feedback loop has historically been slow for students and the vast majority of information could be provided with a reasonably robust test suite.

This won't be perfect but we will attempt to preempt the questions we get each semester and provide reasonable feedback to students quickly, while also ensuring that the learning goals of the class are met. Particularly the ability for students to debug a non-trivial deployment.

## What?

### Pre-commit

[Pre-commit](https://pre-commit.com/) is a tool that enables

#### Linting ([pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks))

We leverage pre-commit hooks to ensure some file formatting standards for YAML, end-of-file line endings, and trailing-whitespace. This enables more readable code.

You can copy the `.pre-commit-config.yaml` file from this repo and configure your local `git` repo to leverage `pre-commit` to validate your commits prior to pushing to `GitHub`.

#### [black](https://github.com/psf/black)

Similar to Linting for general files, we leverage `black` to automatically lint `python` files. This makes it very easy for TAs and Instructors to review your code during office hours or when questions are asked in `Slack`.

You can copy the `.pre-commit-config.yaml` file from this repo and configure your local `git` repo to leverage `pre-commit` to validate your commits prior to pushing to `GitHub`.

#### [ruff](https://github.com/astral-sh/ruff)

`ruff` is a tool similar to `black` in that it lints `python` files, but it also handles import sorting and identification of development poor practices to help you write readable and efficient code.

You can copy the `.pre-commit-config.yaml` file from this repo and configure your local `git` repo to leverage `pre-commit` to validate your commits prior to pushing to `GitHub`.

### [pytest](https://github.com/pytest-dev/pytest)

The validation of your `python` code via unit tests in the class will be handled via `pytest`.

### Container Structure Test ([CST](https://github.com/GoogleContainerTools/container-structure-test))

The validation of your `docker` images built in the class will be handled via `container-structure-test`.

You can copy `container-tests-config.yaml` to validate your Docker images locally. The following command is a rough approximation of what you would need to run.

```{bash}
container-structure-test test --config container-tests-config.yaml --image lab1:latest
```

## How?

Copy the `GitHub` workflow located at `.github/workflows/test.yml` to the same in your repo. This will automatically run the test suite anytime you commit to your repository.
