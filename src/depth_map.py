import os

# Change working directory to MiDaS
# FIXME: change example to add MiDaS repository to include paths
os.chdir('/content/MiDaS')

# Import MiDaS utils
from torchvision.transforms import Compose, Resize, ToTensor
import numpy as np
from midas.midas_net import MidasNet
from PIL import Image

def image_to_depthmap(image: Image) -> np.ndarray:
  # Load the MiDaS model
  model_path = "/content/model-f6b98070.pt"
  model = MidasNet(model_path, non_negative=True)
  transform = Compose([Resize((384, 384)), ToTensor()])

  # Convert the image to a PyTorch tensor and normalize it
  img_tensor = transform(image).unsqueeze(0)
  img_tensor = img_tensor - img_tensor.min()
  img_tensor = img_tensor / img_tensor.max()

  # Use the model to generate a depth map
  with torch.no_grad():
      depth_map = model.forward(img_tensor)

  # Normalize the depth map to the range [0, 1] for visualization
  depth_map = depth_map.squeeze().cpu().numpy()
  depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min())
  return depth_map