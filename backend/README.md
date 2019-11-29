# Project TT Backend

Requirements 
- conda

# Installing requirements

Install `conda` for package management by visit the anaconda website (https://www.anaconda.com/), go to Download > Python 3.7 version. Once you have installed this, you should be able to run "conda" command in your terminal. 

```bash
$ conda
```

Install required packages for Python using `conda`:

```bash
$ conda env create --file project_tt_env.yaml
```

Then activate the environment by running:
```bash
$ source activate project_IP
```

If new package needs to be added, you can use `conda install <package_name>` or `pip install <package_name>`. Then, 
```bash
$ conda env export > project_tt_env.yaml
```

# backend structure

```bash
|-- data
|   |-- london
|   |   └-- 20191124
|   |   |   |-- london_20191124.csv
|   |   |   |-- images
|   |   |   └-- thumbnails
|   |   └-- ...
|   |-- ...
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

# Testing

- We use `pytest` for testing the code.

```bash
$ pytest project_TT/backend
```


# Coding guide

- we use `flake8` for formatting.

```bash
$ flake8 project_TT/backend
```
