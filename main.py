import os
from Canvas import Canvas, Shape
from CDA import CDA


def clearBMPs():
    for file in os.listdir():
        if file.endswith(".bmp"):
            os.remove(file)
            print(f"File {file} removed!")


if __name__ == "__main__":
    clearBMPs()

    testLine = [(0, 0), (0, 10), (0, -10), (10, 0), (-10, 0), (10, 10), (-10, 10), (10, -10), (-10, -10)]
    c = Canvas()
    c.addObject(Shape(testLine, "Black"))

    crds = (-5, 48, 21, 13)
    shift = 5
    rounds = ["ceil", "floor", "int", "math"]
    colours = ["Black", "DimGray", "Gray", "DarkGray", "Silver"]

    for i in range(0, 4):
        c.addObject(Shape(
            CDA(crds[0] + shift * i, crds[1], crds[2] + shift * i, crds[3], rounds[i]),
            colours[i])
        )


    c.saveToFile()
    #c.showImage()
    #c.showImageWithPaint()
    print("All done!")