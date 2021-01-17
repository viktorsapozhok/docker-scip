FROM python:3.9-slim

# install compilers and scip deps
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        libgfortran4 \
        libcliquer1 \
        libopenblas-dev \
        libgsl23 \
        libtbb2 \
        wget \
    && wget -O libboost.deb "http://archive.ubuntu.com/ubuntu/pool/main/b/boost1.65.1/libboost-program-options1.65.1_1.65.1+dfsg-0ubuntu5_amd64.deb" \
    && dpkg -i libboost.deb \
    && rm libboost.deb

# add scip installer inside container
ADD SCIPOptSuite-7.0.2-Linux-ubuntu.deb /

# install scip and remove installer
RUN dpkg -i SCIPOptSuite-7.0.2-Linux-ubuntu.deb \
    && rm SCIPOptSuite-7.0.2-Linux-ubuntu.deb

# create user
RUN groupadd --gid 1000 user \
    && useradd --uid 1000 --gid 1000 --create-home --shell /bin/bash user \
    && chown -R "1000:1000" /home/user

# move script inside the container
RUN mkdir /home/user/scripts
ADD knapsack.py /home/user/scripts

USER user

# install scip python api
RUN pip install pyscipopt

WORKDIR /home/user

CMD tail -f /dev/null
