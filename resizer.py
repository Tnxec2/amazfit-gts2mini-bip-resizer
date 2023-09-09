from PIL import Image
import os, sys
from typing import Tuple
import math
import argparse

class Resizer:
    def __init__(self, 
                 outputdir: str = 'resized', 
                 scale: Tuple[float, float] = None, 
                 backgroundcolor = None, # tuple(0-255, 0-255, 0-255) : R,G,B 
                 removealpha = False, 
                 alphatreshold = 0,
                 invert = False, 
                 noscale = False,
                noantialiased = False ):
        self.outputdir = outputdir
        self.backgroundcolor = backgroundcolor
        self.removealpha = removealpha
        self.alphatreshold = alphatreshold
        self.invert = invert
        self.noscale = noscale
        self.noantialiased = noantialiased
        if (scale):
            (self.scalex, self.scaley) = scale

        parser = argparse.ArgumentParser()
        parser.add_argument('path', nargs='+', help='path to image or directory for scale')
        parser.add_argument('-n', '--noscale', action='store_true', help='no scale images')
        parser.add_argument('-i', '--invert', action='store_true', help='invert color of images')
        parser.add_argument('-r', '--removealpha', action='store_true', help='remove alpha channel of images')
        parser.add_argument('-at', '--alphatreshold', action='store_true', help='value of alpha channel, to use with removealpha param, value: 0-255, example: -at 128')
        parser.add_argument('-na', '--noantialiased', action='store_true', help='not antialiased scale')
        parser.add_argument('-b', '--backgroundcolor', type=int, nargs=3, action='append', help='background color for replace alpha channel, format: R G B, example: -b 255 255 0)')
        parser.add_argument('-x', '--scalex', type=float, help='scale factor horizontaly, examle 0.5')
        parser.add_argument('-y', '--scaley', type=float, help='scale factor verticaly, example 0.5')
        parser.add_argument('-o', '--outputdir', type=str, default='resized', help='output directory name, default = resized')
        self.args, unknown = parser.parse_known_args()
     

    def process(self):
        for inputFileName in self.args.path:
            isDirectory = os.path.isdir(inputFileName)
            isFile = os.path.isfile(inputFileName)
            if not isDirectory and not isFile:
                print("Direcotry %s doesn't exists." % (inputFileName, ))
                sys.exit(1)
            elif isFile:
                if (not inputFileName.endswith('png')):
                    print("Only png image files allowed.")
                    sys.exit(1)
                self.resizeFile(inputFileName)
            elif not isDirectory:
                print("Only directory allowed.")
                sys.exit(1)
            else:
                print(f"directory: {inputFileName}")
                self.resizeDirectory(inputFileName)


    def resizeDirectory(self, path: str):
        dirs = os.listdir( path )
        for item in dirs:
            self.resizeFile(path+item)


    def resizeFile(self, filename: str):
        path = os.path.dirname(filename)
        outputDir = os.path.join(path, self.outputdir)
        if not os.path.exists(outputDir):
            os.mkdir(outputDir)
        if os.path.isfile(filename):
            if (filename.lower().endswith('.png')):
                self.resizeImage(filename)
                pass
            elif (filename.lower().endswith('.json')):
                self.resizeJson(filename)


    def resizeImage(self, filename: str):
        path = os.path.dirname(filename)
        outputDir = os.path.join(path, self.outputdir)
        basename = os.path.basename(filename)
        print(f"resize: {filename}")

        im = Image.open(filename).convert('RGBA')

        imResize = im

        if not self.noscale:
            width, height = im.size
            antialiased = None if self.noantialiased else Image.LANCZOS 
            imResize = im.resize(( math.ceil(width * self.scalex), math.ceil(height * self.scaley)), antialiased)

        if self.invert:
            imResize = self.invertImage(imResize)

        #
        # if original image don't has pixels with alpha chanel,
        # then remove alpha chanel from resized image
        #
        
        if self.removealpha or not self.hasHalfTransparency(im):
            widthR, heightR = imResize.size
            alphaTreshold = self.alphatreshold
            for y in range(heightR):
                for x in range(widthR):
                    coordinate = (x, y)
                    color = imResize.getpixel(coordinate)
                    (r, g, b, a) = color
                    if a <= alphaTreshold:
                        imResize.putpixel(coordinate, (r, g, b, 0))
                    else:
                        bgcolor = self.backgroundcolor if self.backgroundcolor else (0, 0, 0)
                        (br, bg, bb) = bgcolor
                        alpha = a/255
                        R = int(br * (1 - alpha) + r * alpha)
                        G = int(bg * (1 - alpha) + g * alpha)
                        B = int(bb * (1 - alpha) + b * alpha)
                        imResize.putpixel(coordinate, (R, G, B))
        elif self.backgroundcolor:
            background = Image.new('RGBA', imResize.size, self.backgroundcolor)
            imResize = Image.alpha_composite(background, imResize)

            
        imResize.save(os.path.join(outputDir, basename))


    def invertImage(self, img: Image):
        r, g, b, a = img.split()
        r, g, b = map(self.invertPoint, (r, g, b))
        return Image.merge(img.mode, (r, g, b, a))
    

    def invertPoint(self, image):
        return image.point(lambda p: 255 - p)



    def hasHalfTransparency(self, image):
        image_data = image.getdata()
        for pixel in image_data:
            (r, g, b, a) = pixel
            if 0 < a < 255:
                return True
        return False


    def resizeJson(self, filename: str):
        path = os.path.dirname(filename)
        outputDir = os.path.join(path, self.outputdir)
        basename = os.path.basename(filename)
        inputFile = open(filename, 'r')
        outputFile = open(os.path.join(outputDir, basename), 'w')
        Lines = inputFile.read().splitlines()
        for line in Lines:
            outputFile.write(self.processJsonLine(line) + '\n')
        inputFile.close()
        outputFile.close()

    
    def processJsonLine(self, line: str):
        if self.noscale:
            return line
        scale = self.getScale(line)
        if scale:
            return self.resizeJsonData(line, scale)
        return line


    def getScale(self, data: str):
        if ':' in data:
            key = self.getJsonKey(data)
            if key in [
                'X',
                'TopLeftX',
                'BottomRightX',
            ]:
                return self.scalex
            if key in [
                'Y',
                'TopLeftY',
                'BottomRightY',
            ]:
                return self.scaley
        return None


    def resizeJsonData(self, line: str, scale: float):
        (key, value, ending) = self.getJsonValue(line)
        oldval = value
        try:
            value = int(int(value) * scale)
        except:
            pass
        print(key, oldval, '=>', value, ending)
        return key + ": " + str(value) + ending


    def getJsonEnding(self, line: str):
        value = line.strip()
        if value.endswith(','):
            return ','
        if value.endswith('}'):
            return '}'
        else:
            return ''
        
    def getJsonKey(self, line: str):
        return line.split(':')[0].strip().strip('"')
    

    def getJsonValue(self, line: str):
        splits = line.split(':')
        value = splits[1].strip()
        return  (splits[0], value.strip(','), self.getJsonEnding(line)) 

