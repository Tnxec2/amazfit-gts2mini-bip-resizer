import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path', nargs='+', help='path to image or directory for scale')
parser.add_argument('-n', '--noscale', action='store_true', help='no scale images')
parser.add_argument('-i', '--invert', action='store_true', help='invert color of images')
parser.add_argument('-r', '--removealpha', action='store_true', help='remove alpha channel of images')
parser.add_argument('-b', '--backgroundcolor', type=int, nargs=3, action='append', help='background color for replace alpha channel, format: R G B, example: -b 255 255 0)')
parser.add_argument('-x', '--scalex', type=float, help='scale factor horizontaly, examle 0.5')
parser.add_argument('-y', '--scaley', type=float, help='scale factor verticaly, example 0.5')
parser.add_argument('-o', '--outputdir', type=str, default='resized', help='output directory name, default = resized')
args = parser.parse_args()
noscale = args.noscale
invert = args.invert
removealpha =  args.removealpha
backgroundcolor = None
if args.backgroundcolor:
    backgroundcolor = tuple(map(tuple, args.backgroundcolor))[0]

scalex = None
if args.scalex or args.scaley:
    if args.scalex:
        scalex = args.scalex
    else:
        scalex = 1
scaley = None
if args.scalex or args.scaley:
    if args.scaley:
        scaley = args.scaley
    else:
        scaley = 1
scale = (scalex, scaley) if scalex and scaley else None
outputdir = args.outputdir
print('noscale', noscale)
print('invert', invert)
print('removealpha', removealpha)
print('backgroundcolor', backgroundcolor)
print('scale', scale)
print('outputdir', outputdir)
resizer = Resizer(outputdir=outputdir, scale=scale, backgroundcolor=backgroundcolor, removealpha=removealpha, invert=invert, noscale=noscale)
resizer.process()