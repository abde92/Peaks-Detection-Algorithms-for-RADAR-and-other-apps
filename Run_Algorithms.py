# Run algorithms to find peaks 
import numpy as np
import scipy as sp
import pandas as pd
import math as mth
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import FindPeaks as fp

#### Synthetic data
L = 100
s = np.random.randn(L)
x_axis = np.arange(L)

s[10:30] = 8

# ----------------------Find Spike ---------------------#
SpikeIndex,SpikeValue = fp.FindSpike(s)
plt.figure(1)
plt.plot(x_axis,s)
#TODO : mark the spike on the plot -Done
plt.plot(x_axis[SpikeIndex],s[SpikeIndex],'rD')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Naive Peak(spike) Finding Algorithm")
plt.show()

# ----- Multiple Peaks Finding - Baseline = Average-----#
peakIndices_Av = fp.FindPeaks_Basline_Av(s)
plt.figure(2)
plt.plot(x_axis,s)
#TODO : mark peaks on the plot - Done
plt.plot(x_axis[peakIndices_Av],s[peakIndices_Av],'rD')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Multpile Peaks Finding Based Average-Basline lgorithm ")
plt.show()

# ----- Multiple Peaks Finding - Baseline = Median-----#

peakIndices_Md = fp.FindPeaks_Basline_Md(s)
plt.figure(3)
plt.plot(x_axis,s)
#TODO : mark peaks on the plot - Done
plt.plot(x_axis[peakIndices_Md],s[peakIndices_Md],'rD')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Multpile Peaks Finding Based Median-Basline lgorithm ")
plt.show()

# ----- Multiple Peaks Finding - Noisy Peaks - Baseline = Average-----#

peakIndices_Smoth, smoothed_s = fp.FindPeaks_Basline_Smoth(s)

fig4 = plt.figure(4)
plt.subplot(211)
plt.plot(x_axis,s,'b--', label='Signal')
plt.legend()
plt.subplot(212)
plt.plot(x_axis,smoothed_s,color='k', label='Smoothed signal')
# #TODO : mark peaks on the plot - Done
plt.plot(x_axis[peakIndices_Smoth],smoothed_s[peakIndices_Smoth],'rD', label='Peaks')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
fig4.suptitle("Multpile Peaks Finding Based  Smoothing and Average-Basline Algorithm ")
plt.legend()
plt.show()

# ----- Wide Peaks Finding - Baseline = Average-----#
peakIndices_FWP = fp.FindWidePeaks(s)
plt.figure(5)
plt.plot(x_axis,s)
#TODO : mark peaks on the plot - Done
plt.plot(x_axis[peakIndices_FWP],s[peakIndices_FWP])
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Wide Peaks Finding Algorithm ")
plt.show()

# ----- Wide Peaks Finding - Dispersion by Standard Deviation -----#
    #Inputs


peaksFinding_Disp = fp.PeaksFinding_Dispersion(s,lag = 4,Influence = 0.7,Threshold = 3)

#### Real FMCW RADAR data
# data_re = pd.read_csv('IQdata.csv')
# I_channel_signal= data_re.I_data
# I_FFT = fft(I_channel_signal)
# plt.plot(np.abs(I_FFT))
# plt.show()