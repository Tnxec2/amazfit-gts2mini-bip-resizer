#!/usr/bin/python

from resizer import Resizer



temp = (280 / 450, 280 / 450)

outputDirName = 'temp'

resizer = Resizer(outputDirName, temp, backgroundcolor = (57, 194, 238), noscale = True, removealpha = True, alphatreshold=128)
resizer.process()
