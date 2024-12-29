import random
import requests
from colorama import init as colorama_init
from colorama import Fore

colorama_init()


# Get word list from GitHub link
def get_words():
    url = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"
    try:
        response = requests.get(url)
        words = response.text.splitlines()
        return words
    except Exception as e:
        print(e)
        return []


def wordle():
    words = get_words()
    if not words:
        print("Sorry, technical difficulties... we can't get the words :(")
    else:
        secret_word = random.choice(words).upper()
        attempts = 6
        word_length = 5

        print(f"Welcome to Wordle! Guess the {word_length}-letter word.")
        print(f"You have {attempts} attempts. Enter your guesses below:")

        for attempt in range(1, attempts + 1):
            guess_valid = False
            guess = ""

            while not guess_valid:
                guess = input(f"{Fore.RESET}Attempt {attempt} / {attempts}: ").strip().upper()

                if len(guess) != word_length:
                    print(f"Invalid word. The word must be exactly {word_length} letters long.")
                    continue
                elif guess.lower() not in words:
                    print("Invalid word. The word must be a valid English word.")
                    continue
                else:
                    guess_valid = True

            feedback = ""
            for i in range(word_length):
                if guess[i] == secret_word[i]:
                    feedback += f"{Fore.LIGHTGREEN_EX}{guess[i]}"
                elif guess[i] in secret_word:
                    feedback += f"{Fore.LIGHTYELLOW_EX}{guess[i]}"
                else:
                    feedback += f"{Fore.RESET}{guess[i]}"

            print(f"Feedback: {feedback}")

            if guess == secret_word:
                print(f"{Fore.RESET}Congratulations! You guessed the word!")
                return

        print(f"{Fore.RESET}That was your last attempt! The word was {secret_word}. Better luck next time!")


wordle()
