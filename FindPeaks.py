# In this module we implement different algorithms to find peaks in a mezasured signal
# Details of these algorithms can be found in this link: https://www.baeldung.com/cs/signal-peak-detection
import numpy as np
import scipy as sp

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



#2. Algorithm : Find multiple peaks (Baseline =  Average)
 # Input : Measured Data
 # Output : Peaks indexe


def FindPeaks_Basline():
    peaksInedxs = []
    peaksValues = []
    
    
    
    return peaksInedxs, peaksValues