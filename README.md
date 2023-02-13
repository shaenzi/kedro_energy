# energy

## Overview

This is a project showcasing the use of kedro [Kedro documentation](https://kedro.readthedocs.io) and [quarto](quarto.org), with a kedro pipeline that gets data from the open government data portals of Zurich and Basel, does a tiny bit of data wrangling, and renders a parametrised notebook for each dataset. The data are about the power consumption of the cities of Zurich, Basel and Winterthur.

## How to install dependencies

Make sure python 3.10 is installed, as well as pipenv by running `pip install pipenv`. Then you can install all dependencies by:

```
pipenv install
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

### IPython
And if you want to run an IPython session with the kedro data catalog available (for e.g. `catalog.list()`), run:

```
kedro ipython
```
