# docker-scip

Building a docker container with the SCIP Optimization Suite (v7.0.2) + Solving optimization
problem (0-1 knapsack problem) with PySCIPOpt inside the container.

## Build docker

Before building a container, you need to download SCIP Optimization Suite (v7.0.2) deb installer.
SCIP is distributed under the Academic License, and you can download it from the [official website](https://www.scipopt.org/index.php#download).

Copy the downloaded .deb package to the root directory (where the Dockerfile is located).

Then to build a docker image, you can just use `docker-compose`:

```shell
    $ docker-compose build
```
