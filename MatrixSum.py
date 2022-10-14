# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:14:39 2021

@author: Shalin_015
"""

x=[[15,12,99],
   [2,9,98],
   [11,10,97]]
y=[[24,11,2],
   [7,6,0],
   [3,7,99]]
r=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        r[i][j]=x[i][j]+y[i][j]
for e in r:
    print(e)