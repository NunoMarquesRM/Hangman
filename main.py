"""
Hangman Game - Main Module

This module implements the core gameplay logic for the Hangman word-guessing game.
It handles the game loop, user input, word display, and win/lose conditions.

The game follows these rules:
- Player has 6 lives to guess the word
- One letter can be guessed at a time
- Duplicate guesses are not counted against lives
- Game ends when word is guessed or lives run out
"""

import random

from hangman_words import word_list
from hangman_art import stages, logo

# Initialize game variables
# Number of lives the player has
lives = 6
# List to track correctly guessed letters
correct_letters = []

# Display game logo
print(logo)

# Select a random word from the word list
chosen_word = random.choice(word_list)
# For debugging purposes, shows the word to guess
print(chosen_word)

# Initialize the word display with underscores
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Main game loop
game_over = False
while not game_over:
    # Display remaining lives
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    
    # Get player's guess
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue

    # Build the display word with guessed letters
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Show current word state
    print("Word to guess: " + display)

    # Handle incorrect guess
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # Check for game over (lives depleted)
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # Check for win condition (no more underscores)
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Display current hangman state
    print(stages[lives])
