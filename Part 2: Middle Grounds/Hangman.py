"""
Program that simulates a hangman game against the computer
    - Selects a random word out of a word bank
    - Asks for a guessed letter
    - Updates game
        - If letter in word, reveal
        - If letter not in word, decrease guesses
    - Repeat until
        - user guesses all letters in word
        - user runs out of guesses
"""

import random


def choose_word():
    """
    :return: a random word from a pre-made word bank
    """

    words = ['python', 'java', 'hangman', 'programming', 'coding', 'developer']
    return random.choice(words)


def display_word(word, guessed_letters):
    """
    Uses the secret word and list of guessed letters to create the display word. Underscores are used to represent
    not guessed words.
    :param word: the secret word
    :param guessed_letters: list of user guessed letters
    :return: a string that reveals all letters of the word that have been guessed
    """

    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'  # Show an underscore for unguessed letters
    return display


def get_guess(guessed_letters):
    """
    Repeats the guess gathering process until the user guesses a letter that has not been previously guessed.
    :param guessed_letters: list of user guessed letters
    :return: a valid guessed letter
    """

    while True:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("Invalid input or you've already guessed that letter. Try again.")
        else:
            return guess


# Step 4: Define the main game function
def play_hangman():
    """
    Main game function that repeats the guessing process until the game is ended with a user success or a user fail.
    :return:
    """

    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = get_guess(guessed_letters)

        # Checks if guess is in the secret word
        if guess in word:
            print(f"Good job! {guess} is in the word!")
        else:
            attempts -= 1
            print(f"Sorry, {guess} is not in the word. You have {attempts} attempts left.")

        guessed_letters.append(guess)

        # Check if the player has guessed all the letters
        if display_word(word, guessed_letters) == word:
            print(f"Congratulations! You've guessed the word '{word}' correctly!")
            break

    if attempts == 0:
        print(f"Game over! The word was '{word}'.")


play_hangman()
