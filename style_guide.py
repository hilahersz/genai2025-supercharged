import math


def get_volume_of_cuboid(
        length: float,
        width: float,
        height: float,
) -> float:
    vol: float = length * width * height
    return vol


def get_angle_between_vectors(
        x1: float,
        y1: float,
        x2: float,
        y2: float,
) -> float:
    nominator: float = x1 * x2 + y1 * y2
    denominator: float = math.sqrt(x1**2 + y1**2) * math.sqrt(x2**2 + y2**2)
    angle: float = math.acos(nominator / denominator)
    return angle
