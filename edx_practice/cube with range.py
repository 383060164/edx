# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:22:05 2017

@author: tiany
"""
x=int(input('enter an interger:'))
for ans in range(0,abs(x+1)):
    if ans**3>=abs(x):
        break
if ans**3 !=abs(x):
    print(x,'is not a perfect cube')
else:
    if x<0:
        ans=-ans
print(f'cube root of {x} is ans')

