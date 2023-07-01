import open3d as o3d
import numpy as np

class DepthMapToSTLParams:
  z: float = -0.2
  depth: float = 0.5

def depthmap_to_mesh(depth_map: np.ndarray, params: DepthMapToSTLParams = DepthMapToSTLParams()) -> o3d.geometry.TriangleMesh:
  # Create a grid of the same size as the depth map
  x = np.linspace(0, 1, depth_map.shape[1])
  y = np.linspace(0, 1, depth_map.shape[0])
  x, y = np.meshgrid(x, y)

  # Create vertices from the grid
  vertices = np.dstack([x, y, np.zeros_like(x)]).reshape(-1, 3)

  triangles = []
  for i in range(depth_map.shape[0] - 1):
    for j in range(depth_map.shape[1] - 1):
      # Vertices indices
      v1 = i * depth_map.shape[1] + j
      v2 = v1 + 1
      v3 = v1 + depth_map.shape[1]
      v4 = v3 + 1

      # Two triangles for each rectangle
      triangles.append([v1, v2, v3])
      triangles.append([v2, v4, v3])

  # Create the mesh
  mesh = o3d.geometry.TriangleMesh()
  mesh.vertices = o3d.utility.Vector3dVector(vertices)
  mesh.triangles = o3d.utility.Vector3iVector(triangles)

  # Create vertices for the perimeter
  perimeter_vertices = []

  # Bottom edge
  for i in range(depth_map.shape[1]):
    v1 = vertices[i]
    v2 = np.copy(v1)
    v2[2] += params.z
    perimeter_vertices.append(v1)
    perimeter_vertices.append(v2)

  # Right edge
  for i in range(depth_map.shape[0]):
    v1 = vertices[(i + 1) * depth_map.shape[1] - 1]
    v2 = np.copy(v1)
    v2[2] += params.z
    perimeter_vertices.append(v1)
    perimeter_vertices.append(v2)

  # Top edge
  for i in range(depth_map.shape[1] - 1, -1, -1):
    v1 = vertices[(depth_map.shape[0] - 1) * depth_map.shape[1] + i]
    v2 = np.copy(v1)
    v2[2] += params.z
    perimeter_vertices.append(v1)
    perimeter_vertices.append(v2)

  # Left edge
  for i in range(depth_map.shape[0] - 2, -1, -1):  # Stop at the second last row
    v1 = vertices[i * depth_map.shape[1]]
    v2 = np.copy(v1)
    v2[2] += params.z
    perimeter_vertices.append(v1)
    perimeter_vertices.append(v2)

  # Create triangles for the perimeter
  for i in range(0, len(perimeter_vertices) - 2, 2):
    # Vertices indices
    v1 = vertices.shape[0] + i
    v2 = v1 + 1
    v3 = v1 + 2
    v4 = v1 + 3

    # Two triangles for each rectangle
    triangles.append([v1, v2, v3])
    triangles.append([v2, v4, v3])

  # Create vertices from the grid
  bottom_vertices = np.dstack([x, y, np.full_like(x, params.z)]).reshape(-1, 3)

  # Displace the vertices in the z direction
  vertices[:, 2] += depth_map.flatten() * params.depth

  # Add the new vertices to the mesh
  mesh.vertices = o3d.utility.Vector3dVector(np.vstack([vertices, np.array(perimeter_vertices), bottom_vertices]))

  for i in range(depth_map.shape[0] - 1):
      for j in range(depth_map.shape[1] - 1):
          # Vertices indices
          v1 = i * depth_map.shape[1] + j + len(vertices) + len(perimeter_vertices)
          v2 = v1 + 1
          v3 = v1 + depth_map.shape[1]
          v4 = v3 + 1

          # Two triangles for each rectangle
          triangles.append([v1, v3, v2])
          triangles.append([v2, v3, v4])

  # Update the triangles in the mesh
  mesh.triangles = o3d.utility.Vector3iVector(triangles)

  # Orient triangles
  mesh.orient_triangles()

  # Compute normals for better visualization
  mesh.compute_vertex_normals()

  # Remove duplicated vertices
  mesh = mesh.remove_duplicated_vertices()

  # Remove duplicated triangles
  mesh = mesh.remove_duplicated_triangles()

  # Remove degenerate triangles
  mesh = mesh.remove_degenerate_triangles()
  return mesh