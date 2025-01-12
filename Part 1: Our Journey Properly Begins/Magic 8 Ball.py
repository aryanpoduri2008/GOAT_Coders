"""
Program that simulates a Magic 8 Ball
    - Asks user for question
    - Prints a random pre-made answer
"""

import random

responses = [
    "It is certain",
    "It is decidedly so",
    "Ask again later",
    "Concentrate and ask again",
    "Don't count on it",
    "Very doubtful"
]

question = input("Ask the Magic 8-Ball a yes or no question: ")
answer = random.choice(responses)

print(answer)
