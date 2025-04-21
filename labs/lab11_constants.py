from typing import Tuple, List

HTTP_OK_STATUS: int = 200
ISO_DATE_FORMAT: str = "%Y-%m-%d"
PALE_PINK_HEX: str = "#F8D3D3"
USD_FORMATTER: str = "${:,.2f}"


COLORS_TYPE = List[Tuple[int, int, int]]

DARK_BLUE_RGB: Tuple[int, int, int] = (0, 0, 139)
PASTEL_COLORS_HEX: List[str] = [
    "#FFB3BA",  # Light Pink
    "#FFDFBA",  # Light Orange
    "#FFFFBA",  # Light Yellow
    "#BAFFC9",  # Light Green
    "#BAE1FF"   # Light Blue
]

PASTEL_COLORS_RGB: COLORS_TYPE = [
    (255, 179, 186),  # Light Pink
    (255, 223, 186),  # Light Orange
    (255, 255, 186),  # Light Yellow
    (186, 255, 201),  # Light Green
    (186, 225, 255)   # Light Blue
]

PI: float = 3.141592653589793