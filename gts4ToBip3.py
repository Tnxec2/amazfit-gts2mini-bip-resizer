#!/usr/bin/python

from resizer import Resizer



# gts4: 390 x 450

scale = (240 / 390, 280 / 450)


outputDirName = 'bip3'

resizer = Resizer(outputDirName, scale, removealpha=True, alphatreshold=128)
resizer.process()
    



