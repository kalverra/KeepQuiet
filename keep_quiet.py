import sys
import numpy as np
import sounddevice as sd
import soundfile as sf

threshold = 41  # Decibel limit where I can start to be heard in the other room
shut_up, sample_rate = sf.read("D:/Projects/Keep_Quiet/shut_up.wav")


def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    decibel_level = np.linalg.norm(indata) * 10
    if decibel_level >= threshold:
        print(decibel_level)
        sd.play(shut_up, sample_rate, blocking=True)


with sd.InputStream(callback=audio_callback):
    input()  # Requires something here to keep the program going. Messy, but don't really care at the moment
