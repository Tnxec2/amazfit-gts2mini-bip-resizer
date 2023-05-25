#!/usr/bin/python

from resizer import Resizer



temp = (280 / 240, 280 / 240)

outputDirName = 'temp'

resizer = Resizer(outputDirName, temp)
resizer.resize()
