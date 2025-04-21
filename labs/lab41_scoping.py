from typing import Dict

import numpy as np


IBM_RETURNS: Dict[str, float] = {
    "2001": 0.15,
    "2002": -0.35,
    "2003": -0.10,
    "2004": 0.05,
}


def get_average_returns(
        net_returns: Dict[str, float],
) -> float:
    gross_returns: np.array = get_gross_returns(net_returns)
    average_returns: float = get_geometric_mean(gross_returns)
    net_average_returns: float = get_net_average_returns(average_returns)
    return net_average_returns


def get_gross_returns(net_returns: Dict[str, float]) -> np.array:
    """
    Convert net returns to gross returns.
    """
    gross_returns: np.array = np.array(
        [1 + net_return for net_return in net_returns.values()]
    )
    return gross_returns


def get_geometric_mean(gross_returns: np.array) -> float:
    """
    Calculate the geometric mean of the gross returns.
    """
    product: float = np.prod(gross_returns)
    n: int = len(gross_returns)
    geometric_mean: float = product ** (1 / n)
    return geometric_mean


def get_net_average_returns(average_returns: float) -> float:
    """
    Convert gross average returns to net average returns.
    """
    net_average_returns: float = average_returns - 1
    return net_average_returns
