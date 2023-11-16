"""Test my zip function."""

__author__ = "730489972"

from lessons.zip import zip


def test_not_equal():
    """Testing to see if lists not equal will return empty."""
    test_list: list[str] = ["Chocolate", "Vanilla"]
    test_list2: list[int] = [1]
    assert zip(test_list, test_list2) == {}


def test_empty():
    """Testing to see if empty list will show with no input."""
    list1: int = []
    list2: int = []
    assert zip(list1, list2) == {}


def test_equal():
    """Testing to see if function properly works."""
    test_list: list[str] = ["Chocolate", "Vanilla"]
    test_list2: list[int] = [1, 2]
    expected = {"Chocolate": 1, "Vanilla": 2}
    assert zip(test_list, test_list2) == expected
