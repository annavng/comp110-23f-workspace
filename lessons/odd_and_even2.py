"""Practice for exam."""

def odd_and_even(list: list[int]) -> list[int]:
    """Creating function to return odd and even indexes."""
    i: int = 0 
    empty: list[int] = []
    for elem in range(0, len(odd_and_even)):
        if list[i] % 2 == 1 and i % 2 == 0:
            empty = empty + list[i]
        else:
            return []
        return empty
