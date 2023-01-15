"""
Class inherits from Words, gets user input and returns unscrambled user input

--- __init__ initializes user input sent from main.py
    Initializes words list to Words.words

--- unscramble getter returns unscrambled word

--- unscramble setter sets unscrambled word
    sorted words lists will contain nested lists of sorted words. Ex: ["apple"] -> [['a', 'e', 'l', 'p', 'p']]
    matches sorted input list with sorted words list elements (which are lists)
    If match found, sets unscrambled variable that match
    Or returns ValueError

"""

from words import Words
import random

class Unscrambler(Words):
    
    def __init__(self, input):
        self._input = str(input).lower()
        self.sorted_words = []
        self.indices = []
        self.unscarmbled_words = []
        super().__init__()


    @property
    def unscramble(self):
        return self.unscarmbled_words
        

    # Unscrambles the word
    @unscramble.setter    
    def unscramble(self, unword):
        unword = []

        # Sorts words of input, and letters of each word in dictionary
        self._input = sorted(self._input)
        for i in range(len(self.words)):
            self.sorted_words.append(sorted(self.words[i]))

        # Matches words and stores indices into list
        for i in range(len(self.sorted_words)):
            if self.sorted_words[i] == self._input:
                self.indices.append(i)

        if len(self.indices) < 1:
            raise ValueError(f"Word/s with this combination, {self._input} do not exist in the dictionary!")

        # Stores words in words list with same indices
        for i in range(len(self.words)):
            for j in range(len(self.indices)):
                if (self.words[i] in self.words[self.indices[j]]) and len(self.words[i]) >= 3:
                    unword.append(self.words[i])
        
        self.unscarmbled_words = list(dict.fromkeys(unword))
