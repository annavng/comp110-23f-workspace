"""Exercise 7- Dict Unit Test."""


__author__ = "730489972"


from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance
from exercises.ex06.dictionary import count


def test_invert() -> None:
    """Testing to see if the function correctly inverts the values."""
    words: dict[str, str] = {"t": "p", "u": "l", "h": "o"}
    expected: dict[str, str] = {"p": "t", "l": "u", "o": "h"}
    assert invert(words) == expected


def test_invert_two() -> None:
    """Testing to see if the function correctly inverts the strings."""
    words: dict[str, str] = {"help": "me", "cook": "out", "make": "her"}
    expected: dict[str, str] = {"me": "help", "out": "cook", "her": "make"}
    assert invert(words) == expected


def test_invert_empty() -> None:
    """Checking to see if an empty list would be returned."""
    words: dict[str, str] = {}
    expect: dict[str, str] = {}
    assert invert(words) == expect


def test_favorite_color_empty() -> None:
    """Checking to see if an empty list would be returned."""
    color: dict[str, str] = {}
    expect: str = ""
    assert favorite_color(color) == expect


def test_favorite_color() -> None: 
    """Checking to see if the repeated color is returned."""
    color: dict[str, str] = {"Annie": "pink", "Candy": "purple", "Julia": "purple"}
    expect: str = "purple"
    assert favorite_color(color) == expect


def test_favorite_color_two() -> None: 
    """Checking to see if the repeated color is returned."""
    color: dict[str, str] = {"Andrew": "blue", "Josh": "green", "Nathan": "green"}
    expect: str = "green"
    assert favorite_color(color) == expect


def test_count_empty() -> None:
    """Checking to see if an empty list would be returned."""
    item: list[str] = []
    expect: dict[str, int] = {}
    assert count(item) == expect


def test_count() -> None:
    """Checking to see if the count is correct."""
    item: list[str] = ["eggs", "apples", "milk", "apples"]
    expect: dict[str, int] = {"eggs": 1, "apples": 2, "milk": 1}
    assert count(item) == expect


def test_count_g() -> None:
    """Checking to see if the count is correct."""
    item: list[str] = ["strawberry", "onion", "milk", "onion"]
    expect: dict[str, int] = {"strawberry": 1, "onion": 2, "milk": 1}
    assert count(item) == expect


def test_count_two() -> None:
    """Checking to see if the count is correct."""
    item: list[str] = ["rings", "rings", "rings", "necklace"]
    expect: dict[str, int] = {"rings": 3, "necklace": 1}
    assert count(item) == expect


def test_alphabetizer_empty() -> None:
    """Checking to see if an empty list would be returned."""
    alpha: list[str] = {}
    expect: dict[str, list[str]] = {}
    assert alphabetizer(alpha) == expect


def test_alphabetizer() -> None:
    """Checking to see if alphabetizer works properly."""
    alpha: list[str] = ["happy", "sad", "mad", "seriously"]
    expect: dict[str, list[str]] = {"h": ["happy"], "s": ["sad", "seriously"], "m": ["mad"]}
    assert alphabetizer(alpha) == expect


def test_alphabetizer_two() -> None:
    """Checking to see if alphabetizer works properly."""
    alpha: list[str] = ["great", "greet", "upset", "good"]
    expect: dict[str, list[str]] = {"u": ["upset"], "g": ["great", "greet", "good"]}
    assert alphabetizer(alpha) == expect


def test_update_attendance_empty() -> None:
    """Checking to see if an empty list would be returned."""
    att: dict[str, list[str]] = {}
    expect: dict[str, list[str]] = {}
    assert alphabetizer(att) == expect


def test_update_attendance_empty_two() -> None:
    """Checking to see if an empty list would be returned."""
    att: dict[str, list[str]] = {}
    expect: dict[str, list[str]] = ""
    assert alphabetizer(att) == expect


def test_update_attendance() -> None:
    """Checking to see if attendance will update."""
    att: dict[str, list[str]] = {"Monday": ["Candy"], "Tuesday": ["Candy", "Annie"]}
    day: str = "Monday"
    student: str = "May"
    expect: dict[str, list[str]] = update_attendance(att, day, student)
    assert update_attendance(att, day, student) == expect


def test_update_attendance_two() -> None:
    """Checking to see if attendance will update."""
    att: dict[str, list[str]] = {"Wednesday": ["Will"], "Friday": ["Nik", "Jade"]}
    day: str = "Friday"
    student: str = "Grace"
    expect: dict[str, list[str]] = update_attendance(att, day, student)
    assert update_attendance(att, day, student) == expect


def test_update_attendance_three() -> None:
    """Checking to see if attendance will update."""
    att: dict[str, list[str]] = {"Monday": ["Candy"], "Tuesday": ["Candy", "Annie"]}
    day: str = "Tuesday"
    student: str = "Mia"
    expect: dict[str, list[str]] = update_attendance(att, day, student)
    assert update_attendance(att, day, student) == expect