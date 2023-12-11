
def value_exists(test_dict: dict[str, int], test_val: int) -> bool:
    i: int = 0
    exist: bool = False
    while i < len(test_dict):
        if test_dict[i] == test_val:
            exist = True
        i += 1
    return exist