# -*- coding: utf-8 -*-


import wave
import numpy as np

wr = wave.open("TheProdigyOmen.wav","r")
# opening output file to compare two song's speed and set its parameters
par = list(wr.getparams())
par[3] = 0  # to open my output file par[3] should be 0 to except syntax error
par = tuple(par)

output = wave.open("output-question2.wav","w")
output.setparams(par)

frame=wr.getframerate()
# setting output file's frame rate increasing %20 of the first file too speed up 
output.setframerate(frame+20*frame/100)

framenum = wr.getnframes()
# counting number of looping frame by frame
count = int(framenum/frame)

# for all frames, datas are taken and written into our output file to copy input signal
for i in range(count):
    output.writeframes(np.frombuffer(wr.readframes(frame), dtype=np.int16))

wr.close()
output.close()

