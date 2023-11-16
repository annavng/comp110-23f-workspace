"""Sunning the elements of a list using different loops."""

__author__ = "730489972"


def w_sum(vals: list[float]) -> float:
    """Using a while loop to add the sum of values."""
    total: float = 0
    idx: int = 0 
    while idx < len(vals):
        total = total + vals[idx]
        idx = idx + 1
    return total


def f_sum(vals: list[float]) -> float:
    """Using a for loop to add the sum of values."""
    total: float = 0
    for val in vals:
        total = total + val
    
    return total


def f_range_sum(vals: list[float]) -> float:
    """Using a for loop with a range to add the sum of values."""
    total: float = 0
    for i in range(len(vals)):
        total = total + vals[i]
    
    return total


def main() -> None:
    """Calling the functions here."""
    print(w_sum([1.0, 9.0, 7.8]))
    print(f_sum([1.0, 9.0, 7.8]))
    print(f_range_sum([1.0, 9.0, 7.8]))


if __name__ == "__main__":
    main()