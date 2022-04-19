import math
import os

from arc_brezenhem import arc_brezenhem
from canvas import canvas, shape
from segment_CDA import segment_CDA
from segment_brezenhem import segment_brezenhem
from circle_brezenhem import circle_brezenhem
from helpful import picDirect


def clearBMPs():
    for file in os.listdir(picDirect):
        if file.endswith(".bmp") or file.endswith(".png"):
            os.remove(picDirect + file)
            print(f"File {file} removed!")


colourNames = ["Red", "Cyan", "Blue", "DarkBlue", "LightBlue",
               "Purple", "Yellow", "Lime", "Magenta", "Silver",
               "Gray", "Black", "Orange", "Brown", "Maroon",
               "Green", "Olive"]
colourIndex = 0


def getNextColour():
    global colourIndex
    toReturn = colourNames[colourIndex]
    colourIndex = 0 if colourIndex == len(colourNames) - 1 else colourIndex + 1
    return toReturn


def test_canvas():
    c = canvas()
    testLine = [(0, 0), (0, 10), (0, -10), (10, 0), (-10, 0), (10, 10), (-10, 10), (10, -10), (-10, -10)]
    c.addObject(shape(testLine, getNextColour()))
    c.saveToFile("test.png")

def test_segment():
    c = canvas()
    crds = (-20, 48, 21, 13)
    shift = 5
    rounds = ["ceil", "floor", "int", "math"]

    c.addObject(
        shape(segment_brezenhem(0, 0, 12, -5),
              getNextColour())
    )

    for i in range(0, 4):
        c.addObject(shape(
            segment_CDA(crds[0] + shift * (i + 1), crds[1], crds[2] + shift * (i + 1), crds[3], rounds[i]),
            getNextColour())
        )
    c.saveToFile("segments.png")


def test_circle():
    c = canvas()
    c.addObject(shape(circle_brezenhem(-100, -5, 4), getNextColour()))
    c.addObject(shape(circle_brezenhem(20, 30, 16), getNextColour()))
    c.addObject(shape(circle_brezenhem(-20, -5, 25), getNextColour()))
    c.addObject(shape(circle_brezenhem(3, 10, 9), getNextColour()))
    c.addObject(shape(circle_brezenhem(0, 0, 5), getNextColour()))
    c.saveToFile("circles.png")


if __name__ == "__main__":
    clearBMPs()
    c = canvas()

    # test_circle()
    # test_segment()
    # test_canvas()

    c.addObject(shape(arc_brezenhem(0, 0, 50, 0, 90), getNextColour()))

    # angles = [0, 45, 90, 135, 180, 225, 270, 315, 360]
    # for i in range(0, len(angles)):
    #     for j in range(i + 1, len(angles)):
    #         cf = canvas()
    #         cf.addObject(shape(arc_brezenhem(0, 0, 100, angles[i], angles[j]), "red"))
    #         cf.saveToFile(f'img_{angles[i]}_{angles[j]}.png')


    c.saveToFile("img.bmp")
    print("All done!")
