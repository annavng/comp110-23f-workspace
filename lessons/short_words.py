"""Practice for exam."""

def short_words(my_list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    char_length: int = 5
    empty_list: list[str] = []
    for elem in my_list:
        if elem > 5:
            print(f"{elem} is too long!")
        else: 
            empty_list = empty_list + elem 
    return empty_list