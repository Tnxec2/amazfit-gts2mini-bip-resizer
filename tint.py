#!/usr/bin/python

from resizer import Resizer



# gts4: 390 x 450

scale = (24/39, 24/39)


outputDirName = 'tint'

resizer = Resizer(outputDirName, scale, tintColor=(217, 233, 217), removealpha=True, alphatreshold=128, )

resizer.process()

