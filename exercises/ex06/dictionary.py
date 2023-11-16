"""Exercise 6 - Dictionary."""


__author__ = "730489972"


def invert(words: dict[str, str]) -> dict[str, str]:
    """Takes a string of words and inverts the strings."""
    empty_str: dict[str, str] = {}  # Creates a empty str for values to go into. 
    for key in words:
        if words[key] == words:
            raise KeyError("the words are the same!")  # If the words are the same, KeyError will occur. 
        val = words[key]
        empty_str[val] = key
    return empty_str


def favorite_color(color: dict[str, str]) -> str:
    """Gives the most repeated color in the dictionary."""
    clr: dict[str, int] = {}
    max: int = 0
    common: str = ""
    for key in color:  # Using a for loop to analyze each key in the dictionary.
        if color[key] not in clr:
            clr[color[key]] = 1
        else:
            clr[color[key]] += 1 
        if clr[color[key]] > max:
            max = clr[color[key]]
            common = color[key]
    return common


def count(item: list[str]) -> dict[str, int]:
    """Count the times the value appears in list.""" 
    empty: dict[str, int] = {}  # Initializing an empty string to keep keys and values.
    for key in item:
        if key in empty:
            empty[key] += 1  # If the key in item is in empty, add a value. 
        else:
            empty[key] = 1
    return empty


def alphabetizer(alpha: list[str]) -> dict[str, list[str]]:
    """Categorizes words with the correct first letter."""
    word_dict: dict[str, list[str]] = {}  # Initializing an empty string to keep values of a list. 
    for word in alpha:
        first = word[0].lower()
        if first not in word_dict:  # If the first word is not in the empty string, add the word to the string. 
            word_dict[first] = []
        word_dict[first].append(word)  # Using append to add a word to the list.
    return word_dict
    

def update_attendance(att: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Update dict for students who are present in class."""
    if day in att:
        if student not in att[day]:
            att[day].append(student)  # For a day in the list, add the student that is within the list. 
    else:
        att[day] = [student]
    return att