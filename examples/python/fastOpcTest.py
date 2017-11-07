#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import fastopc, time
import numpy as np

numLEDs = 60
client = fastopc.FastOPC('localhost:7890')

pixels = np.zeros(numLEDs)
pixels[10] = 100
pixels[11] = 100
pixels[12] = 200

client.putPixels(1, pixels)
