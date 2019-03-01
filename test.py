import sound
import pyaudio
import traceback
import wavemaker

def play_sound(sound):
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=samplingRate,
                    output=True)
    stream.write(volume * sound)

    stream.stop_stream()
    stream.close()

def play_mary_had_a_little_lamb():

    c = sound.createWave(samplingRate, duration, C_NOTE_FREQ)
    d = sound.createWave(samplingRate, duration, D_NOTE_FREQ)
    e = sound.createWave(samplingRate, duration, E_NOTE_FREQ)

    play_sound(e)
    play_sound(d)
    play_sound(c)
    play_sound(d)
    play_sound(e)
    play_sound(e)
    play_sound(e)

def play_when_you_were_young():

    C_NOTE_FREQ = 261.6256
    C_SHARP_NOTE_FREQ = 277.1826
    D_NOTE_FREQ = 293.6648
    E_NOTE_FREQ = 329.6276
    F_NOTE_FREQ = 349.2282
    F_SHARP_NOTE_FREQ = 369.9944
    G_NOTE_FREQ = 391.9954
    G_SHARP_NOTE_FREQ = 415.3047
    A_NOTE_FREQ = 440.0000
    B_NOTE_FREQ = 493.8833

    e = sound.createWave(samplingRate, duration, E_NOTE_FREQ)
    gSharp = sound.createWave(samplingRate, duration, G_SHARP_NOTE_FREQ)
    b = sound.createWave(samplingRate, duration, B_NOTE_FREQ)
    fSharp = sound.createWave(samplingRate, duration, F_SHARP_NOTE_FREQ)
    cSharp = sound.createWave(samplingRate, duration, 554.3653)
    dSharp = sound.createWave(samplingRate, duration, 622.2540)

    combine([e,gSharp,b])   # E Chord
    combine([e,gSharp,b])   # E Chord
    combine([e,gSharp,b])   # E Chord
    combine([fSharp, gSharp, cSharp])   # F# Chord
    combine([gSharp, b, dSharp])   # G#m Chord

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

def test_AmplitudeChange(original, changed):
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=samplingRate,
                    output=True)

    stream.write(volume * original)
    stream.write(volume * changed)

    stream.stop_stream()
    stream.close()

if __name__ == "__main__":

    try:

        # piano note frequencies in Hz (see https://en.wikipedia.org/wiki/Piano_key_frequencies)
        C_NOTE_FREQ = 261.6256
        D_NOTE_FREQ = 293.6648
        E_NOTE_FREQ = 329.6276
        F_NOTE_FREQ = 349.2282
        G_NOTE_FREQ = 391.9954
        A_NOTE_FREQ = 440.0000
        B_NOTE_FREQ = 493.8833

        volume = 1.0
        duration = 2.0
        samplingRate = 44100

        p = pyaudio.PyAudio()
        wm = wavemaker.WaveMaker(samplingRate)

        cNoteSine = wm.createSineWave(C_NOTE_FREQ, duration)
        play_sound(cNoteSine)
        cNoteSquare = wm.createSquareWave(C_NOTE_FREQ, duration)
        play_sound(cNoteSquare)
        cNoteSawtooth = wm.createSawtoothWave(C_NOTE_FREQ, duration)
        play_sound(cNoteSawtooth)

        wave1 = sound.createWave(samplingRate, duration, 900)
        wave2 = sound.createWave(samplingRate, duration, 440)
        wave3 = sound.createWave(samplingRate, duration, 600)
        wave3_1 = sound.createWave(samplingRate, duration, 600, 4)

        #play_mary_had_a_little_lamb()
        #play_when_you_were_young()

        #play_combined_sound([wave1, wave2], playIndivSounds=True)
        #play_combined_sound([wave1, wave2, wave3], playIndivSounds=True)

    except:
        print(traceback.format_exc())
    finally:
        p.terminate()