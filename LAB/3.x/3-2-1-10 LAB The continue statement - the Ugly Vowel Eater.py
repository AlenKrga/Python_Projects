# Prompt the user to enter a word
user_word = str(input("Enter a word: "))

# Convert the word to uppercase
user_word = user_word.upper()

# Loop through each letter in the word
for letter in user_word:
    # Check if the letter is a vowel using conditional execution and the continue statement
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        # If the letter is not a vowel, print it to the screen
        print(letter)
