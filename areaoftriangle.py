# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:31:47 2021

@author: Shalin_015
"""
print("Enter size to find area of triangle")
f=float(input("Enter First side :"))
s=float(input("Enter Second side :"))
t=float(input("Enter Third side :"))
a=(f+s+t)/2
area=(a*(a-f)*(a-s)*(a-t))**0.5
print("Area of triangle is ",area)