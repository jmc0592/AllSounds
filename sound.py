import numpy as np

def createWave(samplingRate, duration, frequency, amplitude=1.0, returnXCoords=False):
    # samples = np.arange(samplingRate * duration) / samplingRate
    # sinwave = 2 * np.pi * samples * frequency
    # wave = (amplitude * np.sin(sinwave)).astype(np.float32)
    # return wave
    x = createXCoordinates(samplingRate, duration)
    if returnXCoords:
        return createYCoordinates(samplingRate, x, frequency, amplitude=amplitude), x
    return createYCoordinates(samplingRate, x, frequency, amplitude=amplitude)


def createXCoordinates(samplingRate, duration):
    return np.arange(samplingRate * duration)

def createYCoordinates(samplingRate, samples, frequency, amplitude=1.0):
    sinwave = 2 * np.pi * samples * frequency / samplingRate
    wave = (amplitude * np.sin(sinwave)).astype(np.float32)

    return wave