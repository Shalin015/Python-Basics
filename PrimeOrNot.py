# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:40:09 2021

@author: Shalin_015
"""

print("Enter value to check is the value is a prime number or not")
num=int(input("Enter a value :"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if flag:
    print(num,'is not a prime number')
else:
    print(num,'is a prime number')
                