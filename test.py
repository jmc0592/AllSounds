import sound
import pyaudio
import traceback

# TODO: Add test_NCombined() ?

def test_combined(sounds):
    wave = 0
    for sound in sounds:
        # add all sounds together
        wave += sound

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=samplingRate,
                    output=True)

    # play indiv sounds, followed by combined sound
    for sound in sounds:
        stream.write(volume * sound)
    stream.write(volume * wave)

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

    wave1 = sound.createWave(samplingRate, duration, 900)
    wave2 = sound.createWave(samplingRate, duration, 440)
    wave3 = sound.createWave(samplingRate, duration, 600)
    wave3_1 = sound.createWave(samplingRate, duration, 600, 4)

    test_combined([wave1, wave2])
    test_combined([wave1, wave2, wave3])
    test_AmplitudeChange(wave3, wave3_1)

except:
    print(traceback.format_exc())
finally:
    p.terminate()