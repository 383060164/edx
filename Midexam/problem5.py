# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:41:43 2017

@author: tiany
"""
aDict=aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
def uniqueValues(aDict):
    keys=[]
    val=list(aDict.values())
    key=list(aDict.keys())
    for i in range(len(val)):
        count=0
        for j in range(i+1,len(val)):
            if val[i]==val[j]:
                break
            else:
                count+=1
        for k in range(i):
            if val[i]==val[k]:
                break
            else:
                count+=1
        if count==(len(val)-1):
            keys.append(key[i])
    return sorted(keys)  
t=uniqueValues(aDict)
print(uniqueValues(aDict))