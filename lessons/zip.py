"""Combing two lists into a dictionary."""


__author__ = "730489972"


def zip(list: list[str], list2: list[int]) -> dict[str, int]:
    """Produce a dictionary where the keys are the items in first list and the values are the correspoding items of second list."""
    if len(list) != len(list2) or len(list) and len(list2) == 0:
        return {}
    
    list_dict: dict[str, int] = {}
    i: int = 0
    while len(list) > i:
        list_dict[list[i]] = list2[i]
        i = i + 1
    return list_dict 