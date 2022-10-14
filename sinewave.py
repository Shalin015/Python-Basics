# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:37:03 2021

@author: Shalin_015
"""

import numpy as np
import matplotlib.pyplot as plot
time        = np.arange(0, 10, 0.1);
amplitude   = np.sin(time)
plot.plot(time, amplitude)
plot.title('Sine wave')
plot.xlabel('Time')
plot.ylabel('Amplitude = sin(time)')
plot.grid(True)
plot.show()