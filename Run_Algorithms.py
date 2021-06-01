# Run algorithms to find peaks 
import numpy as np
import scipy as sp
import pandas as pd
import math as mth
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import FindPeaks as fp

#### Synthetic data
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

# ----- Multiple Peaks Finding - Baseline = Median-----#

peakIndices_Md = fp.FindPeaks_Basline_Md(s)
plt.plot(x_axis,s)
#TODO : mark peaks on the plot - Done
plt.plot(x_axis[peakIndices_Md],s[peakIndices_Md],'rD')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Multpile Peaks Finding Based Median-Basline lgorithm ")
plt.show()

# ----- Multiple Peaks Finding - Noisy Peaks - Baseline = Average-----#
 
# peakIndices_Smoth = fp.FindPeaks_Basline_Smoth(s)
# plt.plot(x_axis,s)
# #TODO : mark peaks on the plot - Done
# plt.plot(x_axis[peakIndices_Md],s[peakIndices_Md],'rD')
# plt.xlabel('Time(ms)') 
# plt.ylabel('Amplitude(mV)') 
# plt.title("Multpile Peaks Finding Based Median-Basline lgorithm ")
# plt.show()



#### Real FMCW RADAR data
# data_re = pd.read_csv('IQdata.csv')
# I_channel_signal= data_re.I_data
# I_FFT = fft(I_channel_signal)
# plt.plot(np.abs(I_FFT))
# plt.show()