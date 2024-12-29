import random

# The computer picks a random number
secret_number = random.randint(1, 100)
guesses_taken = 0
max_guesses = 7

while guesses_taken < max_guesses:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses_taken += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {guesses_taken} tries.")
        break

if guesses_taken > max_guesses:
    print(f"Sorry, you're out of guesses! The number was {secret_number}.")