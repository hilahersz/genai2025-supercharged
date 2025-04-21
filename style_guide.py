import numpy as np


def get_area(radius: float) -> float:
    area: float = np.pi * radius ** 2
    return area


def get_manhattan_distance(point1: tuple, point2: tuple) -> float:
    distance: float = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return distance
