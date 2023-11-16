"""EX03 - Structured Wordle!!"""

__author__ = "730489972"


def contains_char(word_search: str, character_search: str) -> bool:
    """Character_search will be evaluated through word_search."""
    assert len(character_search) == 1
    index: int = 0
    while len(word_search) > index:  # makes sure that the program won't run over the while loop of the word_search
        # checks if the character_search is within the word_search 
        if word_search[index] == character_search:
            return not False
        else:
            index = index + 1 
    else:
        return False 

# have to define these values before implemented the function that will print the emojis


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess_input: str, secret_word: str) -> str: 
    """Return a str of emojis that coincides with the correct placement of letters within secret and guess."""
    assert len(guess_input) == len(secret_word)
    index_two: int = 0
    emoji_boxes: str = ""  # Keeping an empty string to have a place to put emoji boxes
    while len(secret_word) > index_two:  # making sure that this loop will continue as long as the index_two doesn't become greater than the len(secret_word)
        if secret_word[index_two] == guess_input[index_two]:
            emoji_boxes = emoji_boxes + GREEN_BOX  # Will print out green_box if the charcter matches within the input
        else:
            if contains_char(secret_word, guess_input[index_two]) is False:  # if the function above declares false, a white_box will be printed
                emoji_boxes = emoji_boxes + WHITE_BOX
            else:
                emoji_boxes = emoji_boxes + YELLOW_BOX  # If the function above is not false but the charcter is found within the word at a diff placement, will print yellow_box
        index_two = index_two + 1
    return emoji_boxes


def input_guess(expected_length: int) -> str:
    """Makes sure that the user input is the correct length of characters."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")  # expected length is not a definite int and will be able to change with any word
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    user_turn: int = 1  # int starts at 1 instead of 0 because we are keeping track of how many tries
    status: bool = False
    while status is False and user_turn < 7:  # making sure that the user doesn't get more than 6 turns
        print(f"=== Turn {user_turn}/6 ===")
        user_guess = input_guess(5)
        print(emojified(user_guess, secret_word))  # calling on the emojified function 
        if secret_word == user_guess:
            status = not False
        else: 
            user_turn = user_turn + 1
    if status is True:
        print(f"You won in {user_turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()