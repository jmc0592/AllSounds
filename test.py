import sound
import pyaudio
import time
import matplotlib.pyplot as plt
import traceback

# TODO: Add test_NCombined() ?

def test_TwoCombined(wave1, wave2):
    wave3 = wave1 + wave2

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=samplingRate,
                    output=True)

    stream.write(volume * wave1)
    stream.write(volume * wave2)
    stream.write(volume * wave3) # combined waves

    stream.stop_stream()
    stream.close()
    

def test_ThreeCombined(wave1, wave2, wave3):
    wave4 = wave1 + wave2 + wave3

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=samplingRate,
                    output=True)

    stream.write(volume * wave1)
    stream.write(volume * wave2)
    stream.write(volume * wave3)
    stream.write(volume * wave4) # combined waves

    stream.stop_stream()
    stream.close()

def test_AmplitudeChange(original, changed):
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=samplingRate,
                    output=True)

    stream.write(volume * original)
    stream.write(volume * changed)

    stream.stop_stream()
    stream.close()

try:
    p = pyaudio.PyAudio()

    volume = 1.0
    duration = 2.0
    samplingRate = 44100

    wave1, x1 = sound.createWave(samplingRate, duration, 900, returnXCoords=True)
    wave2, x2 = sound.createWave(samplingRate, duration, 440, returnXCoords=True)
    wave3, x3 = sound.createWave(samplingRate, duration, 600, returnXCoords=True)
    wave3_1, x3_1 = sound.createWave(samplingRate, duration, 600, 4, returnXCoords=True)

    test_TwoCombined(wave1, wave2)
    time.sleep(2)
    test_ThreeCombined(wave1, wave2, wave3)
    time.sleep(2)
    test_AmplitudeChange(wave3, wave3_1)

    # plt.plot(x3, wave3)
    # plt.show()
except:
    print(traceback.format_exc())
finally:
    p.terminate()