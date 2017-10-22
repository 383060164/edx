# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:27:10 2017

@author: tiany
"""
x=int(input('enter the number:'))
epsilon=0.01
step=epsilon**2
numGuess=0
ans=0.0
while abs(ans**2-x)>=epsilon and ans <=x:
    ans=ans+step
    numGuess+=1
print('number of guesses=',numGuess)
if abs(ans**2-x)>=epsilon:
    print('failed on square root of',x)
else:
    print(f"{ans} is close to square rood of {x}")
        
