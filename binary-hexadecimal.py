# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 16:26:54 2021

@author: Shalin015
"""

hexa={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
num=int(input("Enter Binary Number :\n"))

temp=num        
sum=0
i=0
t=""
while temp>0:
    rec=int(temp%10)
    temp=int(temp/10)
    sum=sum+rec*(2**i)
    i+=1
    
while sum>0:
    rec=int(sum%16)
    if rec>9:
        x=hexa.get(rec)
        t=t+x
    else :
        t=t+str(rec)
    sum=int(sum/16)
print("Binary number is :",num)
print("Hexadecimal number is :",t[::-1])
       
        
