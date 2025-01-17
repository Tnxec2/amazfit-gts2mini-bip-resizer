#!/usr/bin/python

from resizer import Resizer




scale = (50 / 70, 50 / 70)

outputDirName = 'scaled'

# resizer = Resizer(outputDirName, scale,  alphatreshold=0, tintColor=(0, 0, 0))
resizer = Resizer('proc', scale, noscale=True,  alphatreshold=10, removealpha=True, backgroundcolor = (113, 119, 108))
resizer.process()
    



