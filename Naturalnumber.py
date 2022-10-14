# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:08:56 2021

@author: Shalin_015
"""

print('Natural Number')
num=int(input("Enter value :"))
if num<0:
    print('Enter positive number')
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
    print('The sum is :',sum)