

#!/usr/bin/python

from resizer import Resizer



# gts2mini: 306 x 354
# bipU: 302 x 320
# bip3: 240 x 280

scaleFactor = (280 / 460, 280 / 460)

outputDirName = 'bip3'

resizer = Resizer(outputDirName, scaleFactor)
resizer.process()
    



