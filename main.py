from shapes.arc_brezenhem import arc_brezenhem
from drawing.canvas import canvas, shape
from shapes.segment_CDA import segment_CDA
from shapes.segment_brezenhem import segment_brezenhem
from shapes.circle_brezenhem import circle_brezenhem
from shapes.rectangle import rectangle
from drawing.colours import getNextColour
from helpful import clearBMPs
from cutting import sutherland


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


def test_arc_brezenhem():
    c = canvas()
    c.addObject(shape(arc_brezenhem(0, 0, 50, 30, 60), getNextColour()))
    c.saveToFile("arc_brezenhem.png")


def test_cutting():
    c = canvas()
    rX1 = -3
    rY1 = -8
    rX2 = 25
    rY2 = 18

    lines = [segment_brezenhem(10, 3, 30, 40),
             segment_brezenhem(-5, 20, 20, -23),
             segment_brezenhem(10, 0, 18, 5),
             segment_brezenhem(6, 6, 2, 30)]

    for line in lines:
        c.addObject(shape(line, "Black"))
        c.addObject(shape(sutherland(rX1, rY1, rX2, rY2, line), "Red"))

    c.addObject(shape(rectangle(rX1, rY1, rX2, rY2), "Blue"))
    c.saveToFile("cutting.png")


def test_all():
    test_circle()
    test_segment()
    test_canvas()
    test_arc_brezenhem()
    test_cutting()


if __name__ == "__main__":
    clearBMPs()
    can = canvas()



    can.saveToFile("img.bmp")
