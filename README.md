# Relief

Convert depth maps to STL files.

This code converts .png depth images create from models like MiDaS (https://github.com/isl-org/MiDaS) to .stl files for 3D printing.

## Setup

To install the required dependencies, run following command:

```sh
$ pip install open3d numpy
```

For `pyenv` user:

Install conda:

```sh
$ pyenv install miniforge3-22.11.1-4
```

Enable conda installation:

```sh
$ pyenv shell miniforge3-22.11.1-4
```

Verify installation:

```sh
$ python --version
Python 3.9.16
$ conda --version
conda 22.11.1
```

Create and activate conda environment from `environment.yaml`:

```sh
$ conda env create -f environment.yaml
$ conda activate relief
```

## Usage

`relief` requires two arguments (input and output folder) and supports one optional parameter to scale the depth map in z direction.

```sh
python run.py --input <input_folder> --output <output_folder>
python run.py --input <input_folder> --output <output_folder> --depth <depth_scale>
```
