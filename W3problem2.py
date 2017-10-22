# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:11:43 2017

@author: tiany
"""

def getGuessedWord(secretWord, lettersGuessed):
    result=''
    for letter in secretWord:
        if letter not in lettersGuessed:
            result=result+'_'
        else:
            result=result+letter
    return result
    

    
    
    
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))            