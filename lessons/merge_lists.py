def merge_lists(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Maps each item in first list to its corresponding item in the second."""
    new_dict: dict[str, int] = {}
    index: int = 0
    
    if len(list1) != len(list2):
        return new_dict
    
    for key in list1:
        new_dict[key[index]] = list2[index]
        index += 1
    return new_dict
