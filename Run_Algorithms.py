# Run algorithms to find peaks 

import numpy as np
import scipy as sp
import math as mth
import matplotlib.pyplot as plt

import FindPeaks as fp


# Generate a synthetic data
L = 1000
s = np.random.randn(L)
x_axis = np.arange(L)
s[100] = 3
s[200] = 5
s[505] = 6


# find spike value and its index in data
output = fp.FindSpike(s)

print(output)
plt.plot(x_axis,s)
#TODO : mark the spike on the plot 
# plt.plot(x_axis,s[peakIndex])
plt.show()








