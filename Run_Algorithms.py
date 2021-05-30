# Run algorithms to find peaks 

import numpy as np
import scipy as sp
import math as mth
import matplotlib.pyplot as plt

import FindPeaks as fp


# Generate a synthetic data
L = 100 
spike = 3
s = np.random.randn(L)
x_axis = np.arange(L)
# find spike value and its index in data
output = fp.FindSpike(s)

print(output)
plt.plot(x_axis,s)
plt.plot(x_axis,s[peakIndex])
plt.show()








