# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:55:59 2021

@author: Shalin015
"""

num=int(input("Enter number 0 to 25:\n"))
if num<=25:
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                print(num,"is not a prime number")
                print(i,"times", num//i,"is",num)
                break
            else:
                print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
else:
    print("Enter less then or equal 25 value")