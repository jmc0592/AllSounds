import sound
import pyaudio
import time
import matplotlib.pyplot as plt
import traceback
import wavemaker

class Freq:
    # piano note frequencies in Hz (see https://en.wikipedia.org/wiki/Piano_key_frequencies)
    C = 261.6256
    CSHARP = DFLAT = 277.1826
    D = 293.6648
    DSHARP = EFLAT = 311.1270
    E = 329.6276
    F = 349.2282
    FSHARP = GFLAT = 369.9944
    G = 391.9954
    GSHARP = AFLAT = 415.3047
    A = 440.0000
    ASHARP = BFLAT = 466.1638
    B = 493.8833

def play_sound(sound):
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=samplingRate,
                    output=True)
    stream.write(volume * sound)

    stream.stop_stream()
    stream.close()

def play_mary_had_a_little_lamb():

    c = sound.createWave(samplingRate, duration, Freq.C)
    d = sound.createWave(samplingRate, duration, Freq.D)
    e = sound.createWave(samplingRate, duration, Freq.E)

    play_sound(e)
    play_sound(d)
    play_sound(c)
    play_sound(d)
    play_sound(e)
    play_sound(e)
    play_sound(e)

def play_when_you_were_young():

    e = sound.createWave(samplingRate, duration, Freq.E)
    gSharp = sound.createWave(samplingRate, duration, Freq.GSHARP)
    b = sound.createWave(samplingRate, duration, Freq.B)
    fSharp = sound.createWave(samplingRate, duration, Freq.FSHARP)
    cSharp = sound.createWave(samplingRate, duration, 554.3653)
    dSharp = sound.createWave(samplingRate, duration, 622.2540)

    play_combined_sound([e,gSharp,b])   # E Chord
    play_combined_sound([e,gSharp,b])   # E Chord
    play_combined_sound([e,gSharp,b])   # E Chord
    play_combined_sound([e,gSharp,b])   # E Chord
    play_combined_sound([fSharp, gSharp, cSharp])   # F# Chord
    play_combined_sound([fSharp, gSharp, cSharp])   # F# Chord
    play_combined_sound([gSharp, b, dSharp])   # G#m Chord

def play_combined_sound(sounds, playIndivSounds=False):
    wave = 0
    for sound in sounds:
        # add all sounds together
        wave += sound

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=samplingRate,
                    output=True)

    # play indiv sounds, followed by combined sound
    if playIndivSounds:
        for sound in sounds:
            stream.write(volume * sound)
    stream.write(volume * wave)

    stream.stop_stream()
    stream.close()

def test_AmplitudeChange():
    original = wm.createSineWave(600, duration)
    changed = wm.createSineWave(600, duration, amplitude=4)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=samplingRate,
                    output=True)

    stream.write(volume * original)
    stream.write(volume * changed)

    stream.stop_stream()
    stream.close()

    #plt.plot(x3, wave3)
    #plt.show() # this bad boi is massive. zoom in to see it.

if __name__ == "__main__":

    try:

        volume = 1.0
        duration = 2.0
        samplingRate = 44100

        p = pyaudio.PyAudio()
        wm = wavemaker.WaveMaker(samplingRate)

        cNoteSine = wm.createSineWave(Freq.C, duration)
        #play_sound(cNoteSine)
        cNoteSquare = wm.createSquareWave(Freq.C, duration)
        #play_sound(cNoteSquare)
        cNoteSawtooth = wm.createSawtoothWave(Freq.C, duration)

        #play_sound(cNoteSine)
        #play_sound(cNoteSquare)
        #play_sound(cNoteSawtooth)
        play_sound(cNoteSquare)

        #test_AmplitudeChange()

        #play_mary_had_a_little_lamb()
        #play_when_you_were_young()

        #play_combined_sound([wave1, wave2], playIndivSounds=True)
        #play_combined_sound([wave1, wave2, wave3], playIndivSounds=True)

        # plt.plot(x3, wave3)
        # plt.show() # this bad boi is massive. zoom in to see it.

    except:
        print(traceback.format_exc())
    finally:
        p.terminate()
