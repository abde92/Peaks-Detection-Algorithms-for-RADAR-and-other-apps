# Peaks finding algorithms
# Details of these algorithms can be found in this link: https://www.baeldung.com/cs/signal-peak-detection
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

#2. Algorithm : Multiple peaks finding (Baseline =  Average)
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

#3. Algorithm : Multiple peaks finding (Baseline =  Median)
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

#4. Algorithm : Multiple Noisy Peaks Finding (Baseline =  Median)=
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
