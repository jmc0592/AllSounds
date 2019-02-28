import pyaudio
import numpy as np
import time
import traceback

def createWave(samplingRate, duration, frequency):
    samples = np.arange(samplingRate * duration) / samplingRate
    sinwave = 2 * np.pi * samples * frequency
    wave = (np.sin(sinwave)).astype(np.float32)

    return wave

try:
    p = pyaudio.PyAudio()

    volume = 1.0
    duration = 2.0
    samplingRate = 44100
    minimumFrequency = 15.0 # Average minimum frequency a human can hear
    maximumFrequency = 20000.0 # Average maximum frequency a human can hear

    # loop though all frequencies and play them
    for frequency in np.arange(minimumFrequency, maximumFrequency, 1):
        print(frequency)

        data = createWave(samplingRate, duration, frequency)

        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=samplingRate,
                        output=True)

        stream.write(volume * data)

        stream.stop_stream()
        stream.close()

except:
    print('oh no')
    print(traceback.format_exc())
finally:
    p.terminate()