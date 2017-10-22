# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:22:05 2017

@author: tiany
"""

def updateHand(hand,word):
    cp=hand.copy()
    for letter in word:
        cp[letter]-=1
    for keys in hand:
        if cp[keys]<=0:
            del cp[keys]
    return cp
#hand = updateHand(hand, 'quail')