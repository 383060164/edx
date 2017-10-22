# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:38:04 2017

@author: tiany
"""
s ='cmbobbqobobababobobjobpsoboboeoboobobobbb'
count=0
flag=0
for char in s:
    if char=='b' and (flag==0 or flag==1):
        flag=1
    elif char=='o' and flag==1:
        flag=2
    elif char=='b' and flag==2:
        count+=1
        flag=1
    else:
        flag=0
print('Number of times bob occurs is:',count)