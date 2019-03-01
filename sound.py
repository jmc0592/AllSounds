import numpy as np

def createWave(samplingRate, duration, frequency, amplitude=1.0):
    samples = np.arange(samplingRate * duration) / samplingRate
    sinwave = 2 * np.pi * samples * frequency
    wave = (amplitude * np.sin(sinwave)).astype(np.float32)

    return wave