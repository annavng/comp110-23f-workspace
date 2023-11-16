def mimic(my_words: str) -> str:
    """Given the string my_words, output the same string"""
    return my_words

mimic("Hello!")
print(mimic("Hello!"))

my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    letter_idx: int = 0
    current_index: int = 0
    if len(my_words) <= letter_idx:
        return ("Index too high!")
    else:
        current_index = current_index + 1