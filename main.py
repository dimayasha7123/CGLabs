import os
from Canvas import Canvas, Shape
from CDA import CDA
from brezenhem import brezenhem


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

    crds = (-20, 48, 21, 13)
    shift = 5
    rounds = ["ceil", "floor", "int", "math"]
    colours = ["Black", "DimGray", "Gray", "DarkGray", "Silver"]

    c.addObject(
        Shape(brezenhem(0, 0, 12, -5),
              colours[0])
    )

    for i in range(0, 4):
        c.addObject(Shape(
            CDA(crds[0] + shift * (i + 1), crds[1], crds[2] + shift * (i + 1), crds[3], rounds[i]),
            colours[i + 1])
        )


    c.saveToFile()
    #c.showImage()
    #c.showImageWithPaint()
    print("All done!")