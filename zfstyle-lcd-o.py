#!/usr/bin/python

from resizer import Resizer



# gts4: 390 x 450

scale = (140/280, 140 /280)


outputDirName = 'bip3'

#resizer = Resizer(outputDirName, scale, noscale=True, tintColor=(0, 24, 25))

resizer = Resizer("orange", scale, noscale=True, removealpha=True, backgroundcolor=(255, 113, 0), alphatreshold=0)
resizer.process()

resizer = Resizer("gray", scale, noscale=True, removealpha=True, backgroundcolor=(103, 123, 121), alphatreshold=0)
resizer.process()

resizer = Resizer("blue", scale, noscale=True, removealpha=True, backgroundcolor=(0, 239, 254), alphatreshold=0)
resizer.process()

resizer = Resizer("green", scale, noscale=True, removealpha=True, backgroundcolor=(0, 187, 0), alphatreshold=0)
resizer.process()
    

