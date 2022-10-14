# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:42:21 2021

@author: Shalin_015
"""

import numpy as np
import matplotlib.pyplot as plt

Marks=np.array([30,50,40,15,12])
Subjects="maths","Science","English","S.S","Hindi"

my_explore=(0,0.1,0,0,0)
plt.pie(Marks,labels=Subjects,autopct="%1.1f%%",shadow=True, explode=my_explore)
plt.title("My Marks")
plt.axis("equal")
plt.show()