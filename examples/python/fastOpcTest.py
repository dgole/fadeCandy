#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import fastopc, time
import numpy as np

numLEDs = 60
client = fastopc.FastOPC('localhost:7890')

pixels = np.zeros([3, numLEDs])
pixels[0,10] = 100
pixels[2,10] = 100
pixels[1,12] = 200

client.putPixels(pixels)
