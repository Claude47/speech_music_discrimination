'''
    features.py
    Prototyping feature extraction
    09/04/2018
'''

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import wave
import sys

def main():
    file = "music_speech/mssp1.wav"
    signal = extract_raw_audio(file) 
    print(signal)
    plt.plot(signal)
    plt.show()
    return

def extract_raw_audio(file): 
    f = wave.open(file,'r')
    sig = f.readframes(-1)
    sig = np.fromstring(sig,'int16')
    return sig

if __name__=="__main__":
    main()
