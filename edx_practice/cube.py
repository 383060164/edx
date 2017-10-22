# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:57:23 2017

@author: tiany
"""
x=int(input('enter an interger:'))
ans=0
while ans**3 < abs(x):
    ans=ans+1
if ans**3!= abs(x):
    print(x,'is not a perfect cube!')
else:
    if x<0:
        ans=-ans
    print('cube rood of',x,'is',ans)
   
