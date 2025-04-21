from typing import List
import math

GOLDEN_RATIO: float = (1 + 5 ** 0.5) / 2
PI: float = 3.141592653589793
KM_TO_MILES: float = 0.621371


def get_median(numbers: List[float]) -> float:
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]
    

def get_standard_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return math.sqrt(sum((x - mean) ** 2 for x in numbers) / len(numbers))


def get_mean(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)  