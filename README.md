# pix2pix from scratch

An attempt at creating a pix2pix implementation from scratch, using only Tensorflow as a dependency.

https://www.tensorflow.org/tutorials/generative/pix2pix

## Setup

I'm using [Anaconda](https://www.anaconda.com/) to set up my Python 3 environment.

Initialize a new environment with Tensorflow as a dependency:

```
conda create -n pix2pix -c anaconda tensorflow-gpu matplotlib jupyterlab pydot
```

Activate the new environment:

```
conda activate pix2pix

```

Start Jupyter Lab:

```
jupyter lab
```

## In Docker

```bash
docker pull tensorflow/tensorflow:latest-gpu-jupyter
```

````

```bash
docker run -it --rm -v $PWD:/tmp -w /tmp -p 8888:8888 --gpus all tensorflow/tensorflow:latest-gpu-jupyter
````
