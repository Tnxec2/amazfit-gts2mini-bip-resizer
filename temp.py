#!/usr/bin/python

from resizer import Resizer



temp = (240 / 348, 280 / 442)

outputDirName = 'temp'

resizer = Resizer(outputDirName, temp, backgroundcolor=(236,237,199), removealpha=True)
resizer.process()
