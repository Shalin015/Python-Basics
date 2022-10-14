# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 16:15:36 2021

@author: Shalin015
"""

num=int(input("Enter Binary Number :\n"))
temp=num
sum=0
i=0
a=0

while temp>0:
    rec=int(temp%10)
    temp=int(temp/10)
    sum=sum+rec*(2**i)
    i+=1
    
while sum>0:
    rec=int(sum%8)
    sum=int(sum/8)
    a=a*10+rec
    
st=str(a)
print("Binary number is :",num)
print("Octal number is :",st[::-1])