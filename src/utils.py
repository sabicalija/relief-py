import os

def validate_directory(path):
    print(f"Validating... {path}")
    if os.path.isdir(path):
        return path
    else:
        raise NotADirectoryError(path)
    
def validate_depth_scale(scale):
    scale = float(scale)
    if scale > 0 and scale <= 1:
        return scale
    else:
        return float(1)