# -*- coding: utf-8 -*-


import wave
import numpy as np

#opening input file to read
wr = wave.open("LauraBraniganSelfControl.wav","r")

# setting parameters
par = list(wr.getparams())
par[3] = 0  # to open my output file par[3] should be 0 to except syntax error
par = tuple(par)

# opening output file to write and set parameter to input's parameters
ww = wave.open("output-question1.wav","w")
ww.setparams(par)

# for less reverb and echo we have to increase freq
freq = 50

sec = wr.getframerate()//freq
# number of frame in file
count = int(wr.getnframes()/sec) 
#shift my file 200 Hz
shift = 200//freq  

for i in range(count):
    # making DFT, rolling and Inverse FT into datas reading from input file
    data = np.frombuffer(wr.readframes(sec),dtype=np.int16)
    left, right = data[0::2], data[1::2]  
    lf, rf = np.fft.rfft(left), np.fft.rfft(right)
    lf, rf = np.roll(lf, shift), np.roll(rf, shift)
    lf[0:shift],rf[0:shift] = 0,0
    nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
    # combining left and right channel with fourier transform
    combine = np.column_stack((nl, nr)).ravel().astype(np.int16)
    ww.writeframes(combine.tostring())
wr.close()
ww.close()