import random


# Step 1: Define a function to pick a random word
def choose_word():
    words = ['python', 'java', 'hangman', 'programming', 'coding', 'developer']
    return random.choice(words)


# Step 2: Define a function to display the current state of the word
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'  # Show an underscore for unguessed letters
    return display


# Step 3: Define a function to handle the guessing process
def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("Invalid input or you've already guessed that letter. Try again.")
        else:
            return guess

# Step 4: Define the main game function
def play_hangman():
    word = choose_word()  # The secret word
    guessed_letters = []  # To track the guessed letters
    attempts = 6  # Number of wrong guesses allowed

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = get_guess(guessed_letters)

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


# Step 5: Start the game
play_hangman()
