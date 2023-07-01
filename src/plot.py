from PIL import Image
import open3d as o3d
import numpy as np

def plot_result(mesh: o3d.geometry.TriangleMesh, image: Image, depth_map: np.ndarray) -> None:
  color = "gray" # = "viridis"
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.imshow(image)
  ax1.axis("off")
  ax1.set_title("Original")
  ax2.imshow(depth_map, cmap=color)
  ax2.axis("off")
  ax2.set_title("Depth Map")
  fig.colorbar(ax2.imshow(depth_map, cmap=color), ax=ax2)
  o3d.visualization.draw_plotly([mesh], up=[0, -1, 0], front=[0, 0, 0.2], lookat=[-0.5, 0.5, 0])