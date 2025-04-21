def get_reversed_string(s: str) -> str:
    string_reversed: str = s[::-1]
    return string_reversed


def is_odd(n: int) -> bool:
    odd_check: bool = n % 2 != 0
    return odd_check


def is_even(n: int) -> bool:
    even_check: bool = n % 2 == 0
    return even_check
