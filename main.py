import os
from Canvas import Canvas


def clearBMPs():
    for file in os.listdir():
        if file.endswith(".bmp"):
            os.remove(file)
            print(f"File {file} removed!")



if __name__ == "__main__":
    testLine = [(3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4), (0, 0)]
    clearBMPs()
    c = Canvas()
    c.addObject(testLine)
    c.saveToFile()
    #c.showImage()
    #c.showImageWithPaint()
    print("All done!")