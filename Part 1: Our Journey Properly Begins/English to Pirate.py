"""
Program that converts an English statement into pirate-speak
    - Asks for an English statement
    - Uses dictionary to convert individual words
    - Prints priate-speak version

Ex: "hello, i am your friend" -> "ahoy, i be yer matey"
"""

import re

pirate_dict = {
    "hello": "ahoy",
    "hi": "ahoy",
    "my": "me",
    "friend": "matey",
    "is": "be",
    "are": "be",
    "you": "ye",
    "your": "yer",
    "the": "th'",
    "of": "o'",
    "yes": "aye",
    "no": "nay",
    "excuse me": "avast",
    "stop": "belay",
    "money": "booty",
    "treasure": "booty",
    "i am": "I be",
    "you're": "ye be",
    "good": "fine",
    "bad": "bilge",
    "thank you": "thank ye",
    "where": "whar",
    "sir": "captain",
    "madam": "wench",
    "man": "lubber",
    "woman": "lass",
    "go": "sail",
    "left": "port",
    "right": "starboard"
}

print("Welcome to the pirate translator!")
sentence = input("Give me an english sentence to translate into pirate-speak: ").lower()

for word, pirate_word in pirate_dict.items():
    sentence = re.sub(word, pirate_word, sentence)

print(f"Here is the translation: {sentence}")