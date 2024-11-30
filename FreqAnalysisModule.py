# %%
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def FreqAnalysis(data, fs, N, N2, sclNum):

    freq_vec = (np.array(range(1,N2+1)) * fs /(2*N2) )/ 1e6  # [MHz]
    fft_data = np.fft.fft(data, axis = 0)
    mag_data = np.abs(fft_data)  
    if data.ndim == 3:
        for i in range(0,sclNum):
            fig = go.Figure()
            pltData = mag_data[0:N2, :, i]
            pltMean = np.mean(pltData, axis=1)
            
            fig.add_trace(go.Scatter(x=freq_vec, y=pltMean,
                    mode='lines',
                    name='lines'))
               
            fig.show()
            del fig           

    else:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=freq_vec, y=mag_data,
                    mode='lines',
                    name='lines'))
    
    
    

    
    

# %%


