# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 12:28:34 2017

@author: tiany
"""

s = 'beggh'
l=len(s)
counter1=0
longest=s[0]
out=s[0]
for i in range(0,l-1):
    if s[i]<=s[i+1]:
        out=out+s[i+1]
        if len(out)>counter1:
            counter1=len(out)
            longest=out
    else:
        out=s[i+1]
print('Longest substring in alphabetical orderis: '+longest)