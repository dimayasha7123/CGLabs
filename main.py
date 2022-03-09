import os
from Canvas import Canvas
from CDA import CDA


def clearBMPs():
    for file in os.listdir():
        if file.endswith(".bmp"):
            os.remove(file)
            print(f"File {file} removed!")


if __name__ == "__main__":
    testLine = [(0, 0), (0, 10), (0, -10), (10, 0), (-10, 0), (10, 10), (-10, 10), (10, -10), (-10, -10)]
    clearBMPs()
    c = Canvas()
    c.addObject(testLine)
    line1 = CDA(-5, 48, 21, 13, "ceil")
    print(line1)
    c.addObject(line1)
    c.saveToFile()
    #c.showImage()
    #c.showImageWithPaint()
    print("All done!")