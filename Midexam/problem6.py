# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:46:52 2017

@author: tiany
"""
test=(5, (1,2), [[1],[9]])
def max_val(t):
    val=[]
    for i in range(len(t)):
        if type(t[i])==int:
            val.append(t[i])
        else:
            for j in range(len(t[i])):
                if type(t[i][j])==int:
                    val.append(t[i][j])
                else:
                    for z in range(len(t[i][j])):
                        val.append(t[i][j][z])
    ans=max(val)
    return ans
print(max_val(test))        