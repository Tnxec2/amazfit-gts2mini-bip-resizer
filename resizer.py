from PIL import Image
import os, sys
from typing import Tuple
import math

class Resizer:
    def __init__(self, outputdir: str, scale: Tuple[float, float]):
        self.outputdir = outputdir
        (self.scalex, self.scaley) = scale
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('path', nargs='+', help='path to image or directory for scale')
        self.args = parser.parse_args()


    def resize(self):
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
        outputDir = os.path.join(path, self.outputdir)
        if not os.path.exists(outputDir):
            os.mkdir(outputDir)
        for item in dirs:
            self.resizeFile(path+item)


    def resizeFile(self, filename: str):
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
        name, ext = os.path.splitext(basename)
        print(f"resize: {filename}")
        im = Image.open(filename)
        width, height = im.size
        antialiased = Image.LANCZOS
        imResize = im.resize(( math.ceil(width * self.scalex), math.ceil(height * self.scaley)), antialiased)
        #
        # if original image don't has pixels with alpha chanel,
        # then remove alpha chanel from resized image
        #
        if not self.hasHalfTransparency(im):
            widthR, heightR = imResize.size
            for y in range(heightR):
                for x in range(widthR):
                    coordinate = (x, y)
                    color = imResize.getpixel(coordinate)
                    (r, g, b, a) = color
                    if a < 128:
                        imResize.putpixel(coordinate, (r, g, b, 0))
                    else:
                        imResize.putpixel(coordinate, (r, g, b, 255))
        imResize.save(os.path.join(outputDir, basename))


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
    

    def isFirst(self, name: str):
        try:
            return True if int(name) == 0 else False
        except:
            return False
    
