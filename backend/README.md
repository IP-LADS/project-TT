# Project TT Backend


# Requirements

Requirements 
- conda

## Installing requirements

Install `conda` for package management by visit the anaconda website
(https://www.anaconda.com/), go to Download > Python 3.7 version. Once you have
installed this, you should be able to run "conda" command in your terminal.

```bash
$ conda
```

Install required packages for Python using `conda`:

```bash
$ conda env create --file project_tt_env.yml
```

Then activate the environment by running:
```bash
$ source activate project_IP
```

If new package needs to be added, you can use `conda install <package_name>` or
`pip install <package_name>`. Then,

```bash
$ conda env export > project_tt_env.yml
```

# Project Structure (Backend)

```bash
|-- data
|   |-- data.csv
|   |-- images
|   |-- thumbnails
|-- frontend
|   └-- ...
|-- backend
|   |-- core
|   |   |-- analytics
|   |   |-- db
|   |   |-- instagram
|   |   |-- ml
|   |   └-- utils
|   └-- notebooks
```

# Development

It is convenient to use python notebook for development. To start a notebook:
```bash
$ jupyter notebook
```

## Importing `core` module

In order to import our own `core`, make sure to include
`/path/to/project_TT/backend` to your `PYTHONPATH`, or in the beginning of the
notebook:

```python
import sys
sys.path.append('/path/to/project_TT/backend')
```

## autoreloading

By default, the notebook will spawn a new internal python which does not keep
track of changes in the code. If you want the changes to be reflected, include
the following two lines at start:

```python
%load_ext autoreload
%autoreload 2
```


# Testing

- We use `pytest` for testing the code.

```bash
$ pytest project_TT/backend
```

# Data

Our dataset is saved externally -- i.e. the `project_TT/data` is not tracked by
`git` and hence you need to download it separately. Check the slack channel for
the instruction.


# Coding guide

- we use `flake8` for formatting.

```bash
$ flake8 project_TT/backend
```
