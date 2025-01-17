#!/usr/bin/python

from resizer import Resizer

outputDirName = 'temp'

resizer = Resizer(outputDirName, noscale=True, removealpha=True, alphatreshold=0)
resizer.process()
