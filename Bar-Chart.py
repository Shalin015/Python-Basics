# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:01:05 2021

@author: Shalin_015
"""

import numpy as np
import matplotlib.pyplot as plt

Country=np.array(["India","USA","Russia","Canada"])
GDP=np.array([500000,200000,100000,300000])

plt.bar(Country,GDP,color="purple")
plt.title("Country GDP",fontsize=15)
plt.xlabel("Country",fontsize=13)
plt.ylable("GDP",fontsize=13)
plt.grid(True)
plt.show()
