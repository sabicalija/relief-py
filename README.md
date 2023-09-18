# Relief: From Depth Maps to STL Files

"Relief" is a tool designed to convert .png depth images into .stl files suitable for 3D printing. This software allows depth images, such as those created from models like MiDaS (https://github.com/isl-org/MiDaS), to be seamlessly converted into tangible 3D objects.

## Getting Started

The steps below will guide you through setting up and running Relief on your system.

### Prerequisites

Relief relies on a few external dependencies:

- [open3d](https://pypi.org/project/open3d/)
- [numpy](https://pypi.org/project/numpy/)

To install these, run the following command:

```sh
$ pip install open3d numpy
```

### Instructions for `pyenv` Users:

To ensure a smooth running of Relief using `pyenv`, you will need to install and enable conda. Here's how:

1. **Install conda:**

```sh
$ pyenv install miniforge3-22.11.1-4
```

2. **Enable conda installation:**

```sh
$ pyenv shell miniforge3-22.11.1-4
```

3. **Verify installation:**

Your Python and Conda versions should correspond to the ones shown below:

```sh
$ python --version
Python 3.9.16
$ conda --version
conda 22.11.1
```

4. **Create and activate the conda environment from `environment.yaml`:**

```sh
$ conda env create -f environment.yaml
$ pyenv activate relief
```

## Running Relief

To run the Relief tool, it requires two arguments - the input and output folders. It also supports an optional parameter to scale the depth map in the z direction.

The following command will guide you on how to execute Relief:

```sh
python run.py --input <input_folder> --output <output_folder>
python run.py --input <input_folder> --output <output_folder> --depth <depth_scale>
```

Replace `<input_folder>`, `<output_folder>` and `<depth_scale>` with your actual paths and scale value, respectively.

Congratulations, you're now ready to start converting depth maps to STL files using Relief!
