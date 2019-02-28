import pyaudio
import numpy as np
import time
import sys
import traceback

try:
    p = pyaudio.PyAudio()

    volume = 0.5
    duration = 1.0
    samplingRate = 44100

    # loop though all frequencies the human ear can hear
    for frequency in np.arange(15,20000,.01):
        print(frequency)

        sinwave = 2 * np.pi * np.arange(samplingRate * duration) * frequency / samplingRate
        samples = (np.sin(sinwave)).astype(np.float32)

        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=samplingRate,
                        output=True)

        stream.write(volume * samples)

        time.sleep(.25)

        stream.stop_stream()
        stream.close()
except:
    print('oh no')
    print(traceback.format_exc())
finally:
    p.terminate()