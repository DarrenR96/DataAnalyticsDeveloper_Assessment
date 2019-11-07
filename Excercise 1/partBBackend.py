# Darren R.
# 6th/Nov/2019

import string
from collections import Counter


class MissingLetters:
    # Public Class for Part B of Excercise 1

    def GetMissingLetters(self, sentence: str):
        # Function for Part A of Excercise 1

        # Input =   Sentence containing any string
        #
        # Output =  alphabetically sorted list of characters not in string
        #

        # Initialize Alphabet characters
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # Ignore all non-US-ASCII characters
        printable = set(string.printable)
        # Drop all whitespaces and lowercase all chars.
        sentence = sentence.lower()
        sentence = list(filter(lambda x: x in printable,
                               sentence.replace(" ", "")))
        # Subtract Alphabet List from Counter List
        nonLetters = list((Counter(alphabet) - Counter(sentence)).elements())
        # Returns list already sorted (Since alphabet is stored sorted initially)
        return nonLetters
