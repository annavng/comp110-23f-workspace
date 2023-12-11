
def odd_and_even(numbers: list[int]) -> list[int]:
    """Return a new list containing the elements of the input list that are odd and even."""
    new: list[int] = []
    idx: int = 0
    if len(numbers) % 2 != 0:
        return new
    while idx < len(numbers) and len(numbers) % 2 == 0:
        if numbers[idx] % 2 == 1:
            new.append[numbers[idx]]
            idx += 1
    return new