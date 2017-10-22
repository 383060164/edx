# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:54:54 2017

@author: tiany
"""

def playHand(hand, wordList, n):
    score = 0
    while calculateHandlen(hand) > 0:
        # Display the hand
        print('Current Hand:', end=' '); displayHand(hand)     
        # Ask user for input
        guess = str(input('Enter word, or a "." to indicate that you are finished: '))        
        # If the input is a single period:
        if guess == '.':        
            # End the game (break out of the loop)
            break            
        # Otherwise (the input is not a single period):
        else:        
            # If the word is not valid:
            if isValidWord(guess, hand, wordList) == False:            
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.', '\n')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += getWordScore(guess, n)
                print('"'+guess+'"', "earned", getWordScore(guess, n), "points. Total:", score, "points", '\n')
                # Update the hand 
                hand = updateHand(hand, guess)               

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if guess == '.':
        print('Goodbye! Total score:', score, 'points.')
    else:
        print('Run out of letters. Total score:', score, 'points.')   