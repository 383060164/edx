# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:20:09 2017

@author: tiany
"""
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
def getWordScore(word,n):
    length=len(word)
    point=0
    for letter in word:
        point=point+SCRABBLE_LETTER_VALUES[letter]
    point=point*length
    if n== length:
        point+=50
    return point
        