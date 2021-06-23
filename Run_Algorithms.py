# By Abderrahim BELISSAOUI
# If you are student, feel free to use these codes
# If you are professional, let me know , send message here abd.belissaoui@gmail
# Run algorithms to find peaks 
import numpy as np
import scipy as sp
import pandas as pd
import math as mth
from scipy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt
import FindPeaks as fp

# ------------------------------------------ Synthetic Data ---------------------------------#
#### Synthetic data  : sum of sine waves
# define a signal that contains 3 components
def SineWAve(SampleRate,StartTime, EndTime,frq1,frq2,frq3):
    
    StepTime = 50/SampleRate
    t_axis = np.arange(StartTime,EndTime, StepTime)
    s = 0.4*np.sin(2*mth.pi*frq1*t_axis) + 1.5*np.cos(2*mth.pi*frq2*t_axis) +0.9*np.sin(2*mth.pi*frq3*t_axis)
    
    return t_axis, s


t_axis , s = SineWAve(SampleRate = 500,StartTime = 0, EndTime = 10 ,frq1 = 20, frq2 = 80, frq3 = 150)

# Add random signal ( Noise)
L = len(s)
s  = s + np.random.randn(L)

# ------------------------------------------ FMCW RADAR raw data ---------------------------------#
# Read csv data
# Download RADAR I/Q data : https://drive.google.com/file/d/1FiApaaWw0SeDA2giC1a6G4EUcVcLrwZ6/view?usp=sharing

IQ_data = pd.read_csv('/home/vibraf/SelfLearning/Datasets/IQdata.csv', usecols = ["I", "Q"] )
IQ_raw_data = IQ_data["I"] + 1j*IQ_data["Q"]
N = len(IQ_raw_data)
Q_raw_data_F = fft(np.array(IQ_raw_data))
freq = fftfreq(N, 1/(5*10**5))[:N//2]
# IQ_FFT = fftshift(fft(np.array(IQ_raw_data), n=256, axis=- 1))
# s = (np.abs(IQ_FFT))/np.max(np.abs(IQ_FFT))
# freq = fftshift(fftfreq(n=256))
s = 2.0/N * np.abs(Q_raw_data_F[0:N//2])
t_axis = freq 
#TODO: Define frequencies axis then range axis;  Status: Done

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