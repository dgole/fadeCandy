#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import fastopc, time
import numpy as np

numLEDs = 60
client = fastopc.FastOPC('localhost:7890')

pixels = np.zeros([numLEDs, 3])

n = 1
dir = 1
pixels[n, 2] = 255

while True:
	if n == 59:
		dir*=-1
	elif n == 0:
		dir*=-1
	pixels = np.roll(pixels, dir, axis=0)
	client.putPixels(0, pixels)
	n+=dir
	time.sleep(0.2)
