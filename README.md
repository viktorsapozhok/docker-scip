# docker-scip

Building a docker container with the SCIP Optimization Suite (v7.0.2) + Solving optimization
(0-1 knapsack problem) with PySCIPOpt inside the container.

## Why choose SCIP?

SCIP is currently one of the fastest non-commercial solvers for mixed integer programming (MIP) and
mixed integer nonlinear programming (MINLP). It's still regularly updated with several releases during a year. 
In addition, it provides an easy-to-use Python API to the SCIP optimization software (PySCIPOpt). 

## How to build docker?

Before building a container, you need to download the latest version of the SCIP Optimization Suite, currently 
it's 7.0.2 version. SCIP is distributed under the Academic License, and you can download it from the [official website](https://www.scipopt.org/index.php#download).

Note, that you need to download deb installer. Copy it to the root directory (where the Dockerfile is located).

Then to build a docker image, you can just use `docker-compose`:

```shell
    $ docker-compose build
```

When building is over, you can see the new image.

```shell
    $ docker images                                                                                                                                                                  ✔  base Py  11:28:35 
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    scip                v0.1                78791bbde634        14 hours ago        519MB
```

## Running SCIP solver inside docker

## Reference

* [PySCIPOpt: Mathematical Programming in Python with the SCIP Optimization Suite](https://github.com/scipopt/PySCIPOpt)
* [SCIP Optimization Suite](https://www.scipopt.org/)
