# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:24:55 2017

@author: tiany
"""

def genPrimes():
    primes=[]
    x=1
    while True:
        x+=1
        flag=True
        for p in primes:
            if x%p==0:
                flag=False
                break
        if flag:
            primes.append(x)
            yield x
        