'''
	Generates a multitude of different sound waves.
'''

import numpy as np
from scipy import signal as sg

class WaveMaker():

	def __init__(self, samplingRate):
		self.samplingRate = samplingRate

	def createSineWave(self, frequency, duration=2.0):
		return (np.sin(2 * np.pi * np.arange(self.samplingRate * duration) * frequency/self.samplingRate)).astype(np.float32)

	def createSquareWave(self, frequency, duration=2.0):
		return (sg.square(2 * np.pi * np.arange(self.samplingRate * duration) * frequency/self.samplingRate)).astype(np.float32)

	def createSawtoothWave(self, frequency, duration=2.0):
		return (sg.sawtooth(2 * np.pi * np.arange(self.samplingRate * duration) * frequency/self.samplingRate)).astype(np.float32)