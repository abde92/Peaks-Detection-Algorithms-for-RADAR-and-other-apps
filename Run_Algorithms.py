# Run algorithms to find peaks 
import numpy as np
import scipy as sp
import pandas as pd
import math as mth
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import FindPeaks as fp

#### Synthetic data 1 : random data
# L = 100
# s = np.random.randn(L)
# t_axis = np.arange(L)
# s[10:15] = 4

#### Synthetic data 2 : sum of sine waves

def SineWAve(SampleRate,StartTime, EndTime,frq1,frq2,frq3):
    
    StepTime = 50/SampleRate
    t_axis = np.arange(StartTime,EndTime, StepTime)
    s = 0.4*np.sin(2*mth.pi*frq1*t_axis) + 1.5*np.cos(2*mth.pi*frq2*t_axis) +0.9*np.sin(2*mth.pi*frq3*t_axis)
    
    return t_axis, s


t_axis , s = SineWAve(SampleRate = 500,StartTime = 0, EndTime = 10 ,frq1 = 20, frq2 = 80, frq3 = 150)

#### Synthetic data 3: sum of sine waves + noise (randone data)
L = len(s)
s  = s + np.random.randn(L)

#### Real world data :  I/Q data of an FMCW RADAR


# ----------------------Find Spike ---------------------#
SpikeIndex,SpikeValue = fp.FindSpike(s)
plt.figure(1)
plt.plot(t_axis,s)
#TODO : mark the spike on the plot -Done
plt.plot(t_axis[SpikeIndex],s[SpikeIndex],'rD')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Naive Peak(spike) Finding Algorithm")
plt.show()

# ----- Multiple Peaks Finding - Baseline = Average-----#
peakIndices_Av = fp.FindPeaks_Basline_Av(s)
plt.figure(2)
plt.plot(t_axis,s)
#TODO : mark peaks on the plot - Done
plt.plot(t_axis[peakIndices_Av],s[peakIndices_Av],'rD')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Multpile Peaks Finding Based Average-Basline lgorithm ")
plt.show()

# ----- Multiple Peaks Finding - Baseline = Median-----#

peakIndices_Md = fp.FindPeaks_Basline_Md(s)
plt.figure(3)
plt.plot(t_axis,s)
#TODO : mark peaks on the plot - Done
plt.plot(t_axis[peakIndices_Md],s[peakIndices_Md],'rD')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Multpile Peaks Finding Based Median-Basline lgorithm ")
plt.show()

# ----- Multiple Peaks Finding - Noisy Peaks - Baseline = Average-----#

peakIndices_Smoth, smoothed_s = fp.FindPeaks_Basline_Smoth(s)

fig4 = plt.figure(4)
plt.subplot(211)
plt.plot(t_axis,s,'b--', label='Signal')
plt.legend()
plt.subplot(212)
plt.plot(t_axis,smoothed_s,color='k', label='Smoothed signal')
# #TODO : mark peaks on the plot - Done
plt.plot(t_axis[peakIndices_Smoth],smoothed_s[peakIndices_Smoth],'rD', label='Peaks')
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
fig4.suptitle("Multpile Peaks Finding Based  Smoothing and Average-Basline Algorithm ")
plt.legend()
plt.show()

# ----- Wide Peaks Finding - Baseline = Average-----#
peakIndices_FWP = fp.FindWidePeaks(s)
plt.figure(5)
plt.plot(t_axis,s)
#TODO : mark peaks on the plot - Done
plt.plot(t_axis[peakIndices_FWP],s[peakIndices_FWP])
plt.xlabel('Time(ms)') 
plt.ylabel('Amplitude(mV)') 
plt.title("Wide Peaks Finding Algorithm ")
plt.show()


