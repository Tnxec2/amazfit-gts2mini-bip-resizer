

#!/usr/bin/python

from resizer import Resizer



# gts2mini: 306 x 354
# bipU: 302 x 320
# bip3: 240 x 280

scale = (20/33, 20/33)
# scaleGTS2toBIP3 = (240 / 348, 240 / 348)

outputDirName = 'scale'

resizer = Resizer(outputDirName, scale, removealpha=True, alphatreshold=128)
resizer.process()
    



