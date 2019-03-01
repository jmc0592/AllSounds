import numpy as np

def createWave(samplingRate, duration, frequency):
    samples = np.arange(samplingRate * duration) / samplingRate
    sinwave = 2 * np.pi * samples * frequency
    wave = (np.sin(sinwave)).astype(np.float32)

    return wave