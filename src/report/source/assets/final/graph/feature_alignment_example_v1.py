# src/slides/weekly/src/img/disconet/graph/feature_alignment_example_v1.py

# One square feature map [1,C,H,W]; x points right and y points down.
import math
from torch.nn import functional as F

def align_features(
    sender_features, angle_deg, dx, dy
):
    _, C, H, W = sender_features.shape
    a = math.radians(angle_deg)
    cos, sin = math.cos(a), math.sin(a)
    transform = sender_features.new_tensor([
        [cos, -sin, 2 * dx / W],
        [sin,  cos, 2 * dy / H],
        [0,    0,    1],
    ])
    inverse = transform.inverse()
    theta = inverse[:2].unsqueeze(0)
    grid = F.affine_grid(
        theta, (1, C, H, W),
        align_corners=False)
    return F.grid_sample(
        sender_features, grid,
        align_corners=False)
