#!/usr/bin/python

from resizer import Resizer



# gts4: 390 x 450

scale = (140/280, 140 /280)


outputDirName = 'bip3'

#resizer = Resizer(outputDirName, scale, noscale=True, tintColor=(0, 24, 25))

#resizer = Resizer("bluetint", scale, noscale=True, removealpha=True, invert=True, tintColor=(0, 239, 254), alphatreshold=0)
#resizer = Resizer("orangetint", scale, noscale=True, removealpha=True, invert=True, tintColor=(255, 113, 0), alphatreshold=0)
#resizer = Resizer("graytint", scale, noscale=True, removealpha=True, invert=True, tintColor=(103, 123, 121), alphatreshold=0)
#resizer = Resizer("greentint", scale, noscale=True, removealpha=True, invert=True, tintColor=(0, 187, 0), alphatreshold=0)
resizer = Resizer("whitetint", scale, noscale=True, removealpha=True, invert=True, tintColor=(255, 255, 255), alphatreshold=0)
resizer.process()
    

