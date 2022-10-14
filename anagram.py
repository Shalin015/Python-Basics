# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:27:06 2021

@author: Shalin_015
"""

str1=(input('Enter first word :'))
str2=(input('Enter second word :'))
str1=str1.lower()
str2=str2.lower()
if(len(str1)==len(str2)):
    sortstr1=sorted(str1)
    sortstr2=sorted(str2)
    if(sortstr1==sortstr2):
        print(str1,'and',str2,'are anagram.')
    else:
        print(str1,'and',str2,'are not anagram')
else:
    print(str1,'and',str2,'are not anagram')
