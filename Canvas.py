import datetime
import os
from PIL import Image, ImageColor


def transformation(xy, size):
    x = xy[0]
    y = xy[1]
    xSize = size[0]
    ySize = size[1]
    x = x + xSize // 2
    y = y * (-1) + ySize // 2
    return x, y


class Canvas:
    def __init__(self):
        self.objects = []
        self.backgroundColour = "#FDF5E6"
        self.margin = 10
        self.axisColour = "#C5B6C6"
        self.objColour = "#000000"

    def addObject(self, obj):
        self.objects.append(obj)

    def addObjectList(self, objList):
        self.objects.extend(objList)

    def saveToFile(self, path="img"):
        self.getImage().save(path +
                             datetime.datetime.now().strftime("_%d.%m.%y_%H.%M.%S") +
                             ".bmp"
                             if path == "img" else path)

    def showImage(self):
        self.getImage().show()

    def showImageWithPaint(self):
        self.saveToFile("tmp.bmp")
        os.system("mspaint tmp.bmp")
        for file in os.listdir():
            if file == "tmp.bmp":
                os.remove(file)

    def getSize(self):
        left = 0
        right = 0
        up = 0
        down = 0
        for obj in self.objects:
            for pixel in obj:
                x = pixel[0]
                y = pixel[1]
                if x < left:
                    left = x
                if x > right:
                    right = x
                if y < down:
                    down = y
                if y > up:
                    up = y
        xSize = right - left + 1 + 2 * self.margin
        ySize = up - down + 1 + 2 * self.margin
        return xSize, ySize

    def getImage(self):
        size = self.getSize()
        img = Image.new(mode = "RGB", size = size, color = ImageColor.getrgb(self.backgroundColour))

        xSize = size[0]
        ySize = size[1]
        for i in range(0, xSize):
            img.putpixel((i, ySize // 2), ImageColor.getrgb(self.axisColour))
        for j in range(0, ySize):
            img.putpixel((xSize // 2, j), ImageColor.getrgb(self.axisColour))


        for obj in self.objects:
            for pixel in obj:
                img.putpixel(transformation(pixel, size), ImageColor.getrgb(self.objColour))
        return img
