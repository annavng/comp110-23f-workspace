
def multiples(input: list[int]) -> list[bool]:
    """Return a list of bools that tells whether each int value is a multiple of the previous value."""
    empty: list[bool] = []
    i: int = 0
    i2: int = 1
    while i < len(input):
        if input[i] % input[i2] == 0:
            empty += True
        else:
            empty += False
        i2 += 1
        i += 1 
    return empty

