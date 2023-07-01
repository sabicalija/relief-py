import requests
import io
import PIL
import numpy as np

def download(url: str) -> PIL.Image:
  """Download image from URLs.

  Parameters
  ----------
  url : str
    The URL to download the image from.

  Returns
  -------
  PIL.Image
    The downloaded image.
  """
  # Send a HTTP request to the specified URL
  r = requests.get(url, stream = True)
  # If the response was successul, no exception will be raised
  r.raise_for_status()
  # Check if the image was retrieved successfully
  if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    # Open a local file with wb ( write binary ) permission.
    image = PIL.Image.open(io.BytesIO(r.content))
  else:
    print('Image couldn\'t be retreived')
  return image

def convert(input: str, output: str):
  """Convert images of depth maps to numpy arrays.

  Parameters
  ----------
  input : str
    The path of the input folder.
  output : str
    The path of the output folder.

  Returns
  -------
  None
  """
  pass

def depth_map_to_numpy_array(file_path) -> np.ndarray:
  """Convert images of depth maps to numpy arrays.
  
  Parameters
  ----------
  input : str
    The path of the input file.
  
  Returns
  -------
  np.ndarray
    The converted numpy array.
  """
  img = PIL.Image.open(file_path)
  img_gray = img.convert("L")
  depth_map = np.array(img_gray)
  depth_map = depth_map.squeeze()
  depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min())
  return depth_map