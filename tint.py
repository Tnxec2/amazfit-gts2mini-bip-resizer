#!/usr/bin/python

from resizer import Resizer



# gts4: 390 x 450

scale = (140/280, 140 /280)


outputDirName = 'tint'

resizer = Resizer(outputDirName, noscale=True, tintColor=(0, 24, 25))

resizer.process()

