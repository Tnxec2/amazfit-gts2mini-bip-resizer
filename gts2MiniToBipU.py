#!/usr/bin/python

from resizer import Resizer


# gts2mini: 306 x 354
# bipU: 302 x 320
# bip3: 240 x 280

scaleGTS2MINItoBIP3 = (240 / 306, 280 / 354)
scaleBIPUtoBIP3 = (240 / 302, 280 / 320)
scaleGTS2MINItoBIPU = (302 / 306,  320 / 354)


outputDirName = 'bipU'

resizer = Resizer(outputDirName, scaleGTS2MINItoBIPU)
resizer.process()
