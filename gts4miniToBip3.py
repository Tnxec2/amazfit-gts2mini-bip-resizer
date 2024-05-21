#!/usr/bin/python

from resizer import Resizer



# gts4mini: 336 x 388

scale = (240 / 336, 280 / 388)


outputDirName = 'bip3'

resizer = Resizer(outputDirName, scale, removealpha=True, alphatreshold=128)
resizer.process()
    



