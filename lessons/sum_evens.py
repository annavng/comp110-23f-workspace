"""Practive summing over lists"""

def sum_evens_in_lists(input_list: list[int]) -> int:
    """Sum all even numbers in this list."""
    list_sum: int = 0
    for elem in input_list:
        if elem % 2 == 0: # if i can divide by 2 it is even 
            list_sum = list_sum + elem
    return list_sum 