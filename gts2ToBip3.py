

#!/usr/bin/python

from resizer import Resizer



# gts2mini: 306 x 354
# bipU: 302 x 320
# bip3: 240 x 280

scaleGTS2toBIP3 = (240 / 348, 280 / 442)

outputDirName = 'bip3'

resizer = Resizer(outputDirName, scaleGTS2toBIP3)
resizer.resize()
    



