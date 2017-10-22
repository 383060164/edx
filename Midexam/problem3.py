# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:05:07 2017

@author: tiany
"""

def myLog(x,b):
    ans=0
    while b**ans<=x:
        ans+=1
    if b**ans>x:
        return ans-1
    else:
        return ans
print(myLog(41,5))