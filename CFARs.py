
import numpy as np

def ca_cfar(data_matrix, refLength, guardLength, rate_fa):
    alpha = refLength*(rate_fa**(-1/refLength) - 1) # threshold factor calculated done (y)
    
    #TODO square-law detector before performing cfar algorithm !

    cfarWin= np.ones(((refLength+guardLength)*2+1,1))
    cfarWin[refLength+1:refLength+1+2*guardLength]=0
    cfarWin=cfarWin/np.sum(cfarWin)

    #np.reshape(data_matrix, data_matrix.size)
    #np.reshape(cfarWin, cfarWin.size)

    noiseLevel= np.convolve(data_matrix.squeeze(), cfarWin.squeeze(), 'same')
    ca_cfarThreshold = noiseLevel+ alpha

    
    return ca_cfarThreshold

def os_cfar (data_matrix, os_cfar_parms):

    return os_cfarThreshold