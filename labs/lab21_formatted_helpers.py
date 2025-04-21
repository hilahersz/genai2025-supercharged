import math


def get_quadratic_roots(
        a: float,
        b: float,
        c: float,
) -> tuple[float, float]:
    d: float = b**2 - 4 * a * c
    if d < 0:
        raise ValueError("No real roots")
    root1: float = (-b + math.sqrt(d)) / (2 * a)
    root2: float = (-b - math.sqrt(d)) / (2 * a)
    return root1, root2
