# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:48:27 2017

@author: tiany
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    length=0
    for value in hand.values():
        length+=value
    return length