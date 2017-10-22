# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:18:13 2017

@author: tiany
"""

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
print(Square(-10))