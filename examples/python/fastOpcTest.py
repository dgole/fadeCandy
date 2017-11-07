#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import fastopc, time
import numpy as np

numLEDs = 60
client = fastopc.FastOPC('localhost:7890')

pixels = np.zeros([numLEDs, 3])
pixels[10, 0] = 100
pixels[10, 1] = 100
pixels[10, 2] = 100

while True:
	pixels = np.roll(pixels, 1)
	client.putPixels(0, pixels)
	time.sleep(0.05)
