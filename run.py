"""Compute/Convert depth maps to STL
"""
import argparse
import os
import open3d as o3d
from src.utils import validate_directory, validate_depth_scale
from src.image import depth_map_to_numpy_array
from src.mesh import depthmap_to_mesh, DepthMapToSTLParams

def relief(input_path, output_path, depth_scale) -> None:
    """Convert and write depth maps to STL files

    Parameters
    ----------
    input_path : str
        The path of the input folder.
    output_path : str
        The path of the output folder.
    depth_scale : float
        The scale factor of the depth map [0..1].

    Returns
    -------
    None
    """
    for filename in os.listdir(input_path):
        if filename.endswith('.png'):
            file_path = os.path.join(input_path, filename)
            depth_map = depth_map_to_numpy_array(file_path)

            params = DepthMapToSTLParams()
            print(f"Params: {params.depth}")
            params.depth = depth_scale

            print(f"Params: {params.depth}")

            mesh = depthmap_to_mesh(depth_map, params)

            mesh_filename = filename.replace('.png', '.stl')

            o3d.io.write_triangle_mesh(os.path.join(output_path, mesh_filename), mesh)
    pass

def run():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", help="Input directory", type=validate_directory)
    parser.add_argument("-o", "--output", help="Output directory", type=validate_directory)
    parser.add_argument("-d", "--depth", help="Scale of Depth Map [0..1]", type=validate_depth_scale)

    args = parser.parse_args()

    relief(args.input, args.output, args.depth)

if __name__ == "__main__":
    run()