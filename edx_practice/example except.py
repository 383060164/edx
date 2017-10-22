# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:41:32 2017

@author: tiany
"""
while True:
    try:
        n=int(input('enter an integer'))
        break
    except ValueError:
        print('input not an integer,try again')
print('n')
