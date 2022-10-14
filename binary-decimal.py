# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:56:27 2021

@author: Shalin015
"""

num=int(input("Enter Binary number :"))
Binary=num
Decimal=0
base=1
while num>0:
    rec=num%10
    Decimal=Decimal+rec*base
    num=num//10
    base=base*2
print("Binary number is :",Binary)
print("Decimal number is :",Decimal)
