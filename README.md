# pypkgs_ubc 

![](https://github.com/UBC-MDS/pypkgs_ubc/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pypkgs_ubc/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pypkgs_ubc) [![Deploy](https://github.com/UBC-MDS/pypkgs_ubc/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/pypkgs_ubc/actions/workflows/deploy.yml) [![Documentation Status](https://readthedocs.org/projects/pypkgs_ubc/badge/?version=latest)](https://pypkgs_ubc.readthedocs.io/en/latest/?badge=latest)

Demo python package

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ pypkgs_ubc
```

## Features

`catbind` function let's you merge `pandas` categoricals with ease!

## Dependencies

- TODO

## Usage

```
>>> from pypkgs import pypkgs
>>> import pandas as pd
>>> a = pd.Categorical(["character", "hits", "your", "eyeballs"])
>>> b = pd.Categorical(["but", "integer", "where it", "counts"])
>>> pypkgs.catbind(a, b)
[character, hits, your, eyeballs, but, integer, where it, counts]
Categories (8, object): [but, character, counts,
eyeballs, hits, integer, where it, your]
```

## Documentation

The official documentation is hosted on Read the Docs: https://pypkgs_ubc.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/pypkgs_ubc/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
