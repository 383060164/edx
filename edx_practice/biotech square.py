# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:38:58 2017

@author: tiany
"""

x=int(input('give an integer'))
epsilon=0.01
num=0
low=0
high=x
ans=(low+high)/2
while abs(x-ans**2)>epsilon and ans<x:
    print('low=',low,'high=',high,'ans=',ans)
    num+=1
    if ans**2<x:
        low=ans
    else:
        high=ans
    ans=(high+low)/2
print(num)
print(ans)