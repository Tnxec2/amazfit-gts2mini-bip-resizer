#!/usr/bin/python

from resizer import Resizer



temp = (280 / 240, 280 / 240)

outputDirName = 'temp'

resizer = Resizer(outputDirName, temp, backgroundcolor=(255,255,255), noscale=True, invert=True, removealpha=True)
resizer.process()
