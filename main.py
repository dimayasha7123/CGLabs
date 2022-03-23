import os
from canvas import canvas, shape
from segment_CDA import segment_CDA
from segment_brezenhem import segment_brezenhem
from circle_brezenhem import circle_brezenhem


def clearBMPs():
    for file in os.listdir():
        if file.endswith(".bmp"):
            os.remove(file)
            print(f"File {file} removed!")


colourNames = ["red", "Cyan", "Blue", "DarkBlue", "LightBlue",
               "Purple", "Yellow", "Lime", "Magenta", "Silver",
               "Gray", "Black", "Orange", "Brown", "Maroon",
               "Green", "Olive"]
colourIndex = 0


def getNextColour():
    global colourIndex
    toReturn = colourNames[colourIndex]
    colourIndex = 0 if colourIndex == len(colourNames) - 1 else colourIndex + 1
    return toReturn


if __name__ == "__main__":
    clearBMPs()
    c = canvas()

    # testLine = [(0, 0), (0, 10), (0, -10), (10, 0), (-10, 0), (10, 10), (-10, 10), (10, -10), (-10, -10)]
    # c.addObject(shape(testLine, getNextColour()))

    c.addObject(shape(circle_brezenhem(5, 5, 6), getNextColour()))

    # crds = (-20, 48, 21, 13)
    # shift = 5
    # rounds = ["ceil", "floor", "int", "math"]

    # c.addObject(
    #     shape(segment_brezenhem(0, 0, 12, -5),
    #           getNextColour())
    # )

    # for i in range(0, 4):
    #     c.addObject(shape(
    #         segment_CDA(crds[0] + shift * (i + 1), crds[1], crds[2] + shift * (i + 1), crds[3], rounds[i]),
    #         getNextColour())
    #     )

    c.saveToFile()
    # c.showImage()
    # c.showImageWithPaint()
    print("All done!")
