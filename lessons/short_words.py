def short_words(arg: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new: list[str] = []
    i: int = 0
    for elem in arg:
        if arg[i] > 5:
            print(f"{arg[i]} is too long!")
        else:
            new.append(arg[i])
    return new