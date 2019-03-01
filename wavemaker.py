'''
	Generates a multitude of different sound waves.
'''

import numpy as np
from scipy import signal as sg

class WaveMaker():

	def __init__(self, samplingRate):
		self.samplingRate = samplingRate

	def createSineWave(self, frequency, duration=2.0, returnXCoords=False, amplitude=1.0):
		x = self.createXCoordinates(self.samplingRate, duration)
		if returnXCoords:
			return self.createSineYCoordinates(self.samplingRate, x, frequency, amplitude=amplitude), x
		return self.createSineYCoordinates(self.samplingRate, x, frequency, amplitude=amplitude)

	def createSquareWave(self, frequency, duration=2.0):
		return (sg.square(2 * np.pi * np.arange(self.samplingRate * duration) * frequency/self.samplingRate)).astype(np.float32)

	def createSawtoothWave(self, frequency, duration=2.0):
		return (sg.sawtooth(2 * np.pi * np.arange(self.samplingRate * duration) * frequency/self.samplingRate)).astype(np.float32)

	def createXCoordinates(self, samplingRate, duration):
		return np.arange(samplingRate * duration)

	def createSineYCoordinates(self, samplingRate, samples, frequency, amplitude=1.0):
		sinwave = 2 * np.pi * samples * frequency / samplingRate
		wave = (amplitude * np.sin(sinwave)).astype(np.float32)

		return wave