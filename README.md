# Relief

Convert depth maps to STL files.

## Setup

```sh
$ pip install open3d numpy
```

For `pyenv` user:

```sh
$ pyenv install miniforge3-22.11.1-4
```

```sh
$ pyenv shell miniforge3-22.11.1-4
```

```sh
$ python --version
Python 3.9.16
$ conda --version
conda 22.11.1
```

```sh
$ conda env create -f environment.yaml
$ conda activate relief
```

## Usage

```sh
python run.py --input <input_folder> --output <output_folder>
python run.py --input <input_folder> --output <output_folder> --depth <depth_scale>
```
