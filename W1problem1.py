# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:17:12 2017

@author: tiany
"""
s = 'azcbobobegghakl'
numVowels=0
for letter in s:
    if letter=='a' or letter=='e' or letter=='i'\
    or letter=='o' or letter=='u':
        numVowels+=1
print('Number of vowels:',numVowels)
