"""Third Assignment: One Shot Wordle."""

__author__ = "730489972"

# Part 1. establishing a secret and prompting for a guess
secret_word: str = "python"
wordle_input: str = input(f"What is your {len(secret_word)}-letter guess? ")

# using a while loop to get user to use the right amount of letters
expected_length: int = len(secret_word)
while len(wordle_input) != expected_length:
    wordle_input = input(f"That was not {len(secret_word)} letters! Try again: ")
    if len(wordle_input) == expected_length:
        break

# value to start evaluation of index at zero
current_index: int = 0

# setting up a variable to store emojis
emoji_box: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# the while statements will break when the current_index is equal to len(secret_word)
while len(secret_word) > current_index:
    if wordle_input[current_index] == secret_word[current_index]:
        emoji_box = emoji_box + GREEN_BOX
    else:
        # analyzing the same charcter but not in the right place by using a boolean. because i established a different index_two, i am able to cross reference the letters in the wordle_input to all of the letters in the secret_word
        similar_word: bool = False
        index_two: int = 0 
        while similar_word is False and len(secret_word) > index_two:
            if wordle_input[current_index] == secret_word[index_two]:
                similar_word = True
            else:
                index_two = index_two + 1 
        if similar_word is True:
            emoji_box = emoji_box + YELLOW_BOX
        else: 
            emoji_box = emoji_box + WHITE_BOX
    current_index = current_index + 1

print(emoji_box) 

if len(wordle_input) == expected_length and wordle_input == secret_word:
    print("Woo! You got it! ")
if len(wordle_input) == expected_length and wordle_input != secret_word:
    print("Not quite. Play again soon! ")