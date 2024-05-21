#!/usr/bin/python

from resizer import Resizer


# bips: 176 x 176
# gts2mini: 306 x 354
# bipU: 302 x 320
# bip3: 240 x 280

scale = (302 / 176, 302 / 176)
# scaleBIPUtoBIP3 = (240 / 302, 280 / 320)
# scaleGTS2MINItoBIPU = (302 / 306,  320 / 354)

outputDirName = 'bipU'

resizer = Resizer(outputDirName, scale, removealpha=True, alphatreshold=0)
resizer.process()
    



