# docker-scip

Building a docker container with the SCIP Optimization Suite (v7.0.2) + Solving optimization
(0-1 knapsack problem) with PySCIPOpt inside the container.

## Why to choose SCIP

SCIP is currently one of the fastest non-commercial solvers for mixed integer programming (MIP) and
mixed integer nonlinear programming (MINLP). It's regularly updated releasing a new version several times a year. 
In addition, it provides an easy-to-use Python API to the SCIP optimization software (PySCIPOpt). 

## How to build docker

Before building a container, you need to download the latest version of the SCIP Optimization Suite, currently 
it's 7.0.2 version. SCIP is distributed under the Academic License, and you can download it from the [official website](https://www.scipopt.org/index.php#download).

Note, that you need to download deb installer. Copy it to the root directory (where the Dockerfile is located).

Then to build a docker image, you can just use `docker-compose`:

```shell
    $ docker-compose build
```

When building is over, you can see the new image.

```shell
    $ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    scip                v0.1                78791bbde634        14 hours ago        519MB
```

## Running SCIP solver inside docker

To demonstrate how to use PySCIPOpt, we show how to solve a small-scale 
[knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) for the case of multiple knapsacks.

Let's assume that we have a collection of items having different weights and values, and we want to
pack a subset of items into five knapsacks (bins), where each knapsack has a maximum capacity 100, so the 
total packed value is a maximum.

Define a simple container class to store item parameters and initialize 15 items.

```python
class Item:
    def __init__(self, index, weight, value):
        self.index = index
        self.weight = weight
        self.value = value

items = [
    Item(1, 48, 10), Item(2, 30, 30), Item(3, 42, 25), Item(4, 36, 50), Item(5, 36, 35), 
    Item(6, 48, 30), Item(7, 42, 15), Item(8, 42, 40), Item(9, 36, 30), Item(10, 24, 35), 
    Item(11, 30, 45), Item(12, 30, 10), Item(13, 42, 20), Item(14, 36, 30), Item(15, 36, 25)
]
```

Introduce bins (knapsacks) in the similar fashion.

```python
class Bin:
    def __init__(self, index, capacity):
        self.index = index
        self.capacity = capacity

bins = [Bin(1, 100), Bin(2, 100), Bin(3, 100), Bin(4, 100), Bin(5, 100)]
```

As a next step, we create a solver instance.

```python
from pyscipopt import Model

model = Model()
```

## Reference

* [PySCIPOpt: Mathematical Programming in Python with the SCIP Optimization Suite](https://github.com/scipopt/PySCIPOpt)
* [SCIP Optimization Suite](https://www.scipopt.org/)
