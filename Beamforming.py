import numpy as np
def DAS(data,N,activeNum,sclNum,dist_vec,pitch,fs,c):
    timeDelay = np.zeros_like(data)
    beamforming_data = np.zeros_like(data)

    for i in range(0, N):
        for j in range(0, activeNum):
            for k in range(0, sclNum):
                delayDepth = np.sqrt(((k-j)*pitch)**2 + dist_vec[i]**2) + dist_vec[i]
                timeDelay[i,j,k] = delayDepth/c

    delayIndex = np.round(timeDelay * fs)
    delayIndex[delayIndex>N-1] = N-1
    delayIndex[delayIndex<0] = 0    

    for i in range(0,sclNum):
        for j in range(0,activeNum):
            for k in range(0,N):        
                beamforming_data[k,j,i] =  data[int(delayIndex[k,j,i]), j, i]
                
    summation_data= np.squeeze(np.sum(beamforming_data,1))
    return beamforming_data, summation_data


def DMAS(data,N,activeNum,sclNum,dist_vec,pitch,fs,c):
    beamforming_data, _ = DAS(data=data,N=N,activeNum=activeNum,
    sclNum=sclNum,dist_vec=dist_vec,pitch=pitch,fs=fs,c=c)
    y_DMAS = np.zeros((N,sclNum))


    for i in range(sclNum):
        for j in range(activeNum-1):
            for k in range(i+1, activeNum):
                y_DMAS[:,i] += beamforming_data[:, j,i] * beamforming_data[:, k,i]
    return y_DMAS

