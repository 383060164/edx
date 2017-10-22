# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:28:11 2017

@author: tiany
"""
def getAvailableLetters(lettersGuessed):
    import string
    letters=string.ascii_lowercase
    letters=list(letters)
    cop=letters[:]
    for i in letters:
        if i in lettersGuessed: 
            cop.remove(i)
    cop=''.join(cop)
    return cop
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))            