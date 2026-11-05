# Hangman Game - CodeAlpha Python Internship (Task 1)

import random

# list of 5 words
words = ["python", "apple", "computer", "school", "banana"]

# computer picks one word randomly
word = random.choice(words)

guessed = []      # letters the player has guessed
wrong = 0         # how many wrong guesses so far
max_wrong = 6     # player can only be wrong 6 times
won = False

print("Welcome to Hangman!")
print("The word has", len(word), "letters.")

while wrong < max_wrong:

    # make the word to show, like p _ t _ o _
    show = ""
    for letter in word:
        if letter in guessed:
            show = show + letter + " "
        else:
            show = show + "_ "
    print()
    print(show)

    # if there is no _ left, the player found the whole word
    if "_" not in show:
        won = True
        break

    print("Wrong guesses:", wrong, "out of", max_wrong)

    guess = input("Enter a letter: ")
    guess = guess.lower()

    # check the input
    if len(guess) != 1:
        print("Please enter only one letter.")
    elif not guess.isalpha():
        print("Please enter a letter, not a number or symbol.")
    elif guess in guessed:
        print("You already guessed that letter.")
    else:
        guessed.append(guess)
        if guess in word:
            print("Correct!")
        else:
            print("Wrong!")
            wrong = wrong + 1

print()
if won:
    print("You won! The word was", word)
else:
    print("You lost! The word was", word)