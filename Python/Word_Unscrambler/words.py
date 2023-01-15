"""
--- Reads the file
--- Stores every line/word into a list 'words' without new line character
--- Returns those words to unscramble.py

(Makes it easier to alter folders down the road)

NOTE: Use sys function to increase recursive limit so it copies all words into list

"""


import sys
sys.setrecursionlimit(200000)

class Words:

    def __init__(self):
        self.words = []
        with open("words.txt") as fileopen:
            file = fileopen.read()
            self.words = file.split("\n")
        for word in self.words:
            if len(word) < 3:
                i = self.words.index(word)
                self.words.pop(i)
    
    def __str__(self):
        return self.words