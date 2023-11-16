"""Exercise 4- List utility functions."""

__author__ = "730489972"


def all(list: list[int], number: int) -> bool:
    """Checking to see if numbers in list match the number."""
    idx: int = 0  # setting both idx and check to start at the first index 
    check: int = 0
    check1: bool = False
    while len(list) > idx and check1 is False:  # check1 will always be False unless it is changed to True through the if statement
        if number == list[idx]:
            check = check + 1 
        if check == len(list):
            check1 = True
        else:
            idx = idx + 1  # changing the value of idx in order to be able to evaluate all the indices
    return check1


def max(list2: list[int]) -> int: 
    """Finding the highest interger in the list."""
    idx_2: int = 1
    maximum: int = 0
    if len(list2) == 0:
        raise ValueError("max() arg is an empty List")  # if there is no values for the list, then it will argue that the list is empty
    while idx_2 < len(list2):
        if list2[idx_2] > list2[maximum]:  # if the list2 idx_2 is greater than the list2 maximum, it will set a new maximum value until it evaluates all the numbers
            maximum = idx_2
        idx_2 = idx_2 + 1
    return list2[maximum]


def is_equal(list3: list[int], list4: list[int]) -> bool:
    """Checking to see if given a list, integers are equal."""
    i: int = 0 
    check: bool = not True  # the check will be False unless it is proven true
    if len(list3) == 0 and len(list4) == 0:  # making sure the length of both lists are the same
        return True
    if len(list3) != len(list4):
        return not True
    while len(list4) > i and check is False:  # checking to see if the lists are equal, if not, it will run through the indices
        if list3[i] == list4[i]:
            return True
        else:   
            return False
        i = i + 1
    return check