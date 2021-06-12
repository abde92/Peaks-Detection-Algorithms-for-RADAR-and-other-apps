# Peaks finding algorithms
# Details of these algorithms can be found in this link: https://www.baeldung.com/cs/signal-peak-detection
# All functions here return peak indices, only naive peak finding it return both peak indice and peak value
import numpy as np
import pandas as pd
import scipy as sp
import statistics

#1. Algorithm : Find spike (Naive Peak Finding)
 # Input : Measured Data
 # Output : Spike index
def FindSpike(data):
    peakInedx = 0
    peakValue = 0
    for id in range(len(data)):
        
        if  data[id] > peakValue: 
            peakValue = data[id]           
            peakIndex = id
    return peakIndex , peakValue

#2.1 Algorithm : Multiple peaks finding (Baseline =  Average)
 # Input : Measured Data
 # Output : Peaks indices
def FindPeaks_Basline_Av(data):
    peaksIndexs = []
    peak_id = 0
    peak_V = 0
    baseline = statistics.mean(data)

    for id in range(len(data)):
        if  data[id] > baseline: 
            if peak_V == 0 or data[id] > peak_V:
                peak_id = id
                peak_V = data[id]

        elif data[id] < baseline and peak_id != 0:
            peaksIndexs.append(peak_id)        
            peak_id = 0
            peak_V = 0
    if peak_id != 0: 
        peaksIndexs.append(peak_id)       

    return peaksIndexs

#2.2 Algorithm : Multiple peaks finding (Baseline =  Median)
 # Input : Measured Data
 # Output : Peaks indices
def FindPeaks_Basline_Md(data):
    peaksIndices = []
    peak_id = 0
    peak_V = 0
    baseline = statistics.median(data)

    for id in range(len(data)):
        if  data[id] > baseline: 
            if peak_V == 0 or data[id] > peak_V:
                peak_id = id
                peak_V = data[id]

        elif data[id] < baseline and peak_id != 0:
            peaksIndices.append(peak_id)        
            peak_id = 0
            peak_V = 0
    if peak_id != 0: 
        peaksIndices.append(peak_id)       

    return peaksIndices

#3. Algorithm : Multiple Noisy Peaks Finding (Baseline =  Median)=
 # Input : Measured Data
 # Output : Peaks indices
def FindPeaks_Basline_Smoth(data):
    #smoothed = []
    peaksIndices = []
    peak_id = 0
    peak_V = 0
    baseline = statistics.mean(data)
    
    #TODO : Somth data using a moving average 
    # for id in range(len(data)):

        
    #     # smoothed.append(statistics.mean(data[id-2]))
    #     # smoothed.append(statistics.mean(data[id-1]))
    #     # smoothed.append(statistics.mean(data[id]))
    #     # smoothed.append(statistics.mean(data[id+1]))
    #     smoothed.append(statistics.mean(data[id+2]))
    data = pd.DataFrame(data)
    smoothed1 = data.rolling(window=5).mean()
    smoothed = smoothed1.to_numpy()

    for id in range(len(smoothed)):
        if  smoothed[id] > baseline: 
            if peak_V == 0 or smoothed[id] > peak_V:
                peak_id = id
                peak_V = smoothed[id]

        elif smoothed[id] < baseline and peak_id != 0:
            peaksIndices.append(peak_id)        
            peak_id = 0
            peak_V = 0
    if peak_id != 0: 
        peaksIndices.append(peak_id)       

    return peaksIndices, smoothed

    
#4. Algorithm : Detecting Wide Peaks Algorithm
 # Input : Measured Data
 # Output : Peaks indices

def FindWidePeaks(data):
    peakIncices = []
    baseline = statistics.mean(data)
    for id in range(len(data)):
        if  data[id] > baseline: 
            peakIncices.append(id)        
    return peakIncices

#5.1 Algorithm : Dispersion by Standard Deviation
 # Input 1 : Measured Data
 # Input 2 : Lag
 # Input 3 : Influence
 # Input 4 : Threshold
 # Output : Peaks indices
# This is my own DSD algorithm implementation, it does not work ; I
#TODO: I  need to fix an error caused by variance in stdev !
def PeaksFinding_Dispersion (data,lag,Influence,Threshold):
    data = list(data)
    peakIncices = []
    processedSignal = data[0:lag]
    for id in range(lag,len(data)+1):
        y = data[id]
        avr = statistics.mean(processedSignal[id-lag:id])
        # TODO: Fix error provoked by variance in stdev
        sd = statistics.stdev(processedSignal[id-lag:id])
        if y-avr > sd*Threshold:
            peakIncices.append(id)
            adjustedValue = Influence*y + (1-Influence)*processedSignal[id-1]
        else:
            np.append(processedSignal,y) 

    return peakIncices