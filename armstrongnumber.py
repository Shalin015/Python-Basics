# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:07:15 2021

@author: Shalin015
"""

num=int(input("Enter a number :"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"is armstrong number")
else:
    print(num,"is not an armsrong number")