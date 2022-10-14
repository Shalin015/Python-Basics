# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:52:26 2021

@author: Shalin_015
"""

import numpy as np
import matplotlib.pyplot as plt

Balling=np.array([1,2,3,4,5,6,7,8,9,10])
Score=np.array([10,15,12,0,1,3,14,11,19,6])

plt.plot(Balling,Score,color="r",marker=0)
plt.title("Over vs Score",fontsize=15)
plt.xlabel("Over",fontsize=13)
plt.ylabel("Score",fontsize=13)
plt.grid(True)
plt.show()