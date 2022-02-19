import datetime
import os
from enum import Enum
from PIL import Image, ImageColor


class Canvas:
    def __init__(self):
        self.objects = []
        self.backgroundColour = "#FDF5E6"
        self.axisColour = self.backgroundColour

    def addOject(self, obj):
        self.objects.append(obj)

    def addObjectList(self, objList):
        for obj in objList:
            self.addOject(obj)

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
        return (100, 200)

    def getImage(self):
        return Image.new(mode="RGB", size=self.getSize(), color=ImageColor.getrgb(self.backgroundColour))
