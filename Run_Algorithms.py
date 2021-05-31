""" In order to develop and expand my python programming skills, I decided to start 
coding algrithms even in case they are already implemented by other python developers """

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

# ----------------------Find Spike ---------------------#
SpikeIndex,SpikeValue = fp.FindSpike(s)
plt.plot(x_axis,s)
#TODO : mark the spike on the plot -Done
plt.plot(x_axis[SpikeIndex],s[SpikeIndex],'rD')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Naive Peak(spike) Finding Algorithm")
plt.show()

# ----- Multiple Peaks Finding - Baseline = Average-----#
peakIndices_Av = fp.FindPeaks_Basline_Av(s)
plt.plot(x_axis,s)
#TODO : mark peaks on the plot - Done
plt.plot(x_axis[peakIndices_Av],s[peakIndices_Av],'rD')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Multpile Peaks Finding Based Average-Basline lgorithm ")
plt.show()

# ----- Multiple Peaks Finding - Baseline = Average-----#

peakIndices_Md = fp.FindPeaks_Basline_Md(s)
plt.plot(x_axis,s)
#TODO : mark peaks on the plot - Done
plt.plot(x_axis[peakIndices_Md],s[peakIndices_Md],'rD')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Multpile Peaks Finding Based Median-Basline lgorithm ")
plt.show()




