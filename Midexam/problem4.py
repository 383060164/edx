# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:32:34 2017

@author: tiany
"""
aList = ["apple", "cat", "dog", "banana"]
def lessThan4(aList):
    ans=[]
    for ch in aList:
        if len(ch)<4:
            ans.append(ch)
    return ans
print(lessThan4(aList))