"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730489972"

expected_length = 5
word = input("Enter a 5-character word: ")
if len(word) != expected_length:
    print("Error: Word must contain 5 characters ") 
    exit()
else: 
    letter = input("Enter a single character: ")
expected_letter = 1
if len(letter) != expected_letter:
    print("Error: Character must be a single character. ") 
    exit()
else: 
    print("Searching for " + letter + " in " + word)

# Checking Indices for Matches
if (str(word)[0] == str(letter)):
    print(letter + " found at index 0 ")
if (str(word)[1] == str(letter)):
    print(letter + " found at index 1 ")
if (str(word)[2] == str(letter)):
    print(letter + " found at index 2 ")
if (str(word)[3] == str(letter)): 
    print(letter + " found at index 3")
if (str(word)[4] == str(letter)):
    print(letter + " found at index 4 ")

# Counting matching Indices- Single and Multiple
same_character: int = 0

if (str(word)[0] == str(letter)):
    same_character = same_character + 1
if (str(word)[1] == str(letter)):
    same_character = same_character + 1
if (str(word)[2] == str(letter)):
    same_character = same_character + 1
if (str(word)[3] == str(letter)):
    same_character = same_character + 1
if (str(word)[4] == str(letter)):
    same_character = same_character + 1

if (same_character == 1):
    print(str(same_character) + " instance of " + letter + " found in " + word)
if (same_character > 1):
    print(str(same_character) + " instances of " + letter + " found in " + word)

# Couting Matching Indices- No instances
if str(letter) != str(word)[0] and str(letter) != str(word)[1] and str(letter) != str(word)[2] and str(letter) != str(word)[3] and str(letter) != str(word)[4]:
    print("No instances of " + letter + " found in " + word)