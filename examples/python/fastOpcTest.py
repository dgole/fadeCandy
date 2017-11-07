#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import fastopc, time
import numpy as np

numLEDs = 60
client = fastopc.FastOPC('localhost:7890')

pixels = np.zeros([numLEDs, 3])

class Pixels():
    def __init__(self, numLEDs):
		self.numLEDs = numLEDs
		self.array = np.zeros([self.numLEDs, 3])
    def update(self, arrayNew, alphaRise, alphaDecay):
	alpha = arrayNew - self.array
	alpha[alpha > 0.0 ] = alphaRise
	alpha[alpha <= 0.0] = alphaDecay
	self.array = alpha*arrayNew + (1.0-alpha)*self.array 

n = 1
dir = 1
pixels = Pixels(numLEDs)
pixels.array[n,2] = 255
print(pixels.array[:,2])

while True:
	if n == 59:
		dir*=-1
	elif n == 0:
		dir*=-1
	pixels.update(np.roll(pixels.array, dir, axis=0), 1.0, 1.0)
	print(pixels.array[:,2])
	client.putPixels(0, pixels.array)
	n+=dir
	time.sleep(0.2)
