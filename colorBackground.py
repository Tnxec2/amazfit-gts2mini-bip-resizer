#!/usr/bin/python

from resizer import Resizer



temp = (280 / 450, 280 / 450)

outputDirName = 'temp'

resizer = Resizer(outputDirName, temp, (222, 222, 189))
resizer.resize()
