"""
This is a Guess the Word game

A simple game where the computer picks a secret word and you try to guess it a letter at a time.

We practice using for loops and the range() function !
"""

import random # use random choice

# List of possible secret words
WORDS = [
    'mbaam', # donkey
    'gaynde', # lion
    'golo', # monkey
    'xaj', # dog
    'muus', # cat
    'bukki' # hyena
]

# Pick one word randomly from the list to be the secret word
secret_word = random.choice(WORDS)

# Make a list to keep track of the letters the player has guess so far
# At first, all letters are hidden with '_'
guessed_letters = ['_'] * len(secret_word)

MAX_TRIES = 6 # Player can guess up to 6 times

# Tell the player how many letters are in the secret word
print("Guess the secret word! It has", len(secret_word), "letters.")

# This loop lets the player guess up to MAX_TRIES times
for tries in range(MAX_TRIES):
    # Show othe player what letters they have guessed so far
    print("Current word:", ' '.join(guessed_letters))
    # Ask the player to guess a letter
    guess = input("Guess a letter: ")

    # Check each letter in the secret word
    for i in range(len(secret_word)):
        # If the guessed letter matches the letter at position i
        if secret_word[i] == guess:
            # Reveal the letter in the guessed letters list 
            guessed_letters[i] = guess
        
    # If there are no '_' left, the player has guessed the whole word
    if '_' not in guessed_letters:
        print("Congradulations! You guessed the word:", secret_word)
        break # End the game if the word is guessed

# The else belongs to the for loop, not the if!
# It runs if the player didn't break out of the loop (didn't guess the word)
else:
    print("Sorry, you ran out of tries. The word was:", secret_word)