"""
Program that converts an English statement with gen-alpha wordage into an English statement with parent wordage or
vice versa.
    - Gives options to either convert from gen-alpha to parent or parent to gen-alpha
    - Asks for a statement
    - Uses dictionary to convert individual words
    - Prints converted version

Ex: "your outfit is a little crazy dude" -> "your fit is a little wild bruh"
"""

import re

gen_alpha_dict = {
    "cool": "lit",
    "awesome": "fire",
    "suspicious": "sus",
    "amazing": "goated",
    "boring": "lame",
    "embarrassing": "cringe",
    "crazy": "wild",
    "money": "bread",
    "angry": "pressed",
    "smart": "big brain",
    "outfit": "fit",
    "horrible": "dog water",
    "friend": "homie",
    "wow": "sheesh",
    "gossip": "tea",
    "style": "drip",
    "honestly": "not gonna lie",
    "best friend": "twin",
    "enemy": "opp",
    "delusion": "delulu",
    "ok": "bet",
    "dude": "bruh",
    "lying": "capping",
    "charisma": "rizz",
}

print("Welcome to the gen-alpha translator!")
choice = input("Enter 1 if you are a parent translating to gen-alpha, and enter 2 if you are a gen-alpha translating "
               "to parent: ")
sentence = input("Give me a sentence that you want translated: ").lower()
if choice == 1:
    for word, gen_alpha_word in gen_alpha_dict.items():
        sentence = re.sub(word, gen_alpha_word, sentence)
    print(f"Here is the translation: {sentence}")
elif choice == 2:
    for word, gen_alpha_word in gen_alpha_dict:
        sentence = re.sub(gen_alpha_word, word, sentence)
    print(f"Here is the translation: {sentence}")
else:
    print("You didn't choose 1 or 2")