import argparse
import os
from PIL import Image
import numpy as np

def converter(input, output):
    # Iterate over all files in the directory
    for filename in os.listdir(input):
        # Check if the file is a PNG
        if filename.endswith('.png'):
            # Create the full file path by joining the directory and the filename
            file_path = os.path.join(input, filename)
            
            # Open the image file
            img = Image.open(file_path)

            # Convert the image to grayscale (assuming it's a depth map)
            img_gray = img.convert('L')

            # Convert the image data to a numpy array
            depth_map = np.array(img_gray)

            # Normalize the depth map to the range [0, 1]
            depth_map = depth_map.squeeze()
            depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min())

            if output == None:
                output = input

            # Construct the .npy filename by replacing the .png extension
            npy_filename = filename.replace('.png', '.npy')

            # Save the numpy array to a .npy file
            np.save(os.path.join(output, npy_filename), depth_map)

def validate_directory(path):
    if os.path.isdir(path):
        return path
    else:
        raise NotADirectoryError(path)

def main():
    parser = argparse.ArgumentParser(description='Depth Map to Numpy Converter')
    parser.add_argument("-i", "--input",
                        help="Input directory",
                        required=True,
                        type=validate_directory)
    parser.add_argument("-o", "--output",
                        help="Output directory",
                        required=False,
                        type=validate_directory)
    args = parser.parse_args()
    converter(args.input, args.output)

if __name__ == "__main__":
    main()