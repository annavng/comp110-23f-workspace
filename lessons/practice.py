word: str = input("Enter a 5-character word: ")
letter: str = input("Enter a single character: ")


if input("Enter a 5-character word: ")[0] == input("Enter a single character: "):
    print(str(letter) + " found at index 1 ")

print("Hello, " + input("What is your name? ") + "." + " Are you ready to start your chardle? ")
input("Yes or no? ")
print("Great! Let's get to work! ")
        
word: str = input("Enter a 5-character word: ")
if word == len():
    letter: str = input("Enter a single character")
else:
    print("Error: Word must contain 5 characters") + exit ()

if letter != [0]:
    print("Searching for " + letter + " in " + word)
else:
    print("Error: Character must be a single charcter") + exit ()

if str(word)[0] == str(letter):
    print(str(letter) + " found at index 1 ")
if str(word)[1] == str(letter):
    print(str(letter) + " found at index 2 ")
if str(word)[2] == str(letter):
    print(str(letter) + " found at index 3 ")
if str(word)[3] == str(letter): 
    print(str(letter) + " found at index 4 ")
if str(word)[4] == str(letter):
    print(str(letter) + " found at index 5 ")

if str(word)[0] == str(letter):
    print(str(found) + " instance of " + letter + " found in " + str(word))
if str(word)[1] == str(letter):
    print(str(found) + " instance of " + letter + " found in " + str(word))
if str(word)[2] == str(letter):
    print(str(found) + " instance of " + letter + " found in " + str(word))
if str(word)[3] == str(letter):
    print(str(found) + " instance of " + letter + " found in " + str(word))
if str(word)[4] == str(letter):
    print(str(found) + " instance of " + letter + " found in " + str(word))