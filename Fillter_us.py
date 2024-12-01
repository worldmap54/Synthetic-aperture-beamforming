# This function 

import numpy as np
from scipy.signal import firwin, lfilter

def FIR_us(data,numtaps, fs, lowcut=None, highcut=None):
    a_coef = 1.0
    delay_idx = int((numtaps-1)/2)
    if data.ndim == 3:
        padding = np.zeros((delay_idx, 64, 64))
        padding_data = np.concatenate((data, padding), axis=0)
    else:
        padding = np.zeros((delay_idx, 64))
        padding_data = np.concatenate((data, padding), axis=0)

    if lowcut and highcut:  #Bandpass filter:
        cutoff = [lowcut, highcut]
        b_coef = firwin(numtaps, cutoff,window = 'hann' 
                        ,pass_zero = False, fs=fs)

    elif lowcut:            #Lowpass filter:
        cutoff = lowcut
        b_coef = firwin(numtaps, cutoff,window = 'hann' 
                        ,pass_zero = True, fs=fs)  
        
    elif highcut:            #Highpass filter:
        cutoff = highcut
        b_coef = firwin(numtaps, cutoff,window = 'hann' 
                        ,pass_zero = False, fs=fs)             
    else:
        raise ValueError("lowcut 또는 highcut 중 하나는 반드시 입력해야 합니다.")   
    
    
    filtered_data = lfilter(b_coef,a_coef,padding_data, axis=0)
    if data.ndim == 3:
        filtered_data = filtered_data[delay_idx:,:,:]
    else:
        filtered_data = filtered_data[delay_idx:,:]
    return filtered_data