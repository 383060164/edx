# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:06:53 2017

@author: tiany
"""
balance=3329
annualInterestRate=0.2
ini_b=balance
fix=0
while balance>0:
    for month in range(12):
        balance=balance-fix+(balance-fix)*annualInterestRate/12
    if balance>0:
        fix+=10
        balance=ini_b
    elif  balance<=0:
        break
print('Lowest Payment:',fix)    
    
