# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:51:04 2021

@author: Shalin_015
"""

print("Find factorial")
num=int(input("Enter the value:\n"))
fact=1
if num<0:
    print('There is no factorial available in negative number')
elif num==0:
    print('0 factorial is 1')
else:
    for i in range(1,num+1):
        fact=fact*i
    print(num,'factorial is',fact)