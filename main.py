from shapes.arc_brezenhem import arc_brezenhem
from drawing.canvas import canvas, shape
from shapes.segment_CDA import segment_CDA
from shapes.segment_brezenhem import segment_brezenhem
from shapes.circle_brezenhem import circle_brezenhem
from shapes.rectangle import rectangle
from drawing.colours import getNextColour
from helpful import clearPNGs
from cutting import sutherland
from shapes.ngon import NGon


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


def test_identical(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.identical()
    c.addObject(shape(triag.to_pixels(), getNextColour()))
    c.saveToFile("identical.png")


def test_local_scaling(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.local_scale(2, 5)
    c.addObject(shape(triag.to_pixels(), getNextColour()))
    c.saveToFile("local_scale.png")


def test_symmetry(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.symmetry_x()
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.symmetry_y()
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.symmetry_o()
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    c.saveToFile("symmetry.png")


def test_shift(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.shift_x(60)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.shift_y(120)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.shift(-60, -60)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    c.saveToFile("shift.png")


def test_rotation(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.rotation(-90)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    dot = (100, -30)
    triag.rotation_around(-90, dot[0], dot[1])
    c.addObject(shape(triag.to_pixels(), getNextColour()))
    c.addObject(shape([dot], getNextColour()))

    c.saveToFile("rotation.png")


def test_symmetry_diag(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.symmetry_main_diag()
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.symmetry_aux_diag()
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    c.saveToFile("symmetry_diag.png")


def test_common_scaling(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.common_scale(2)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    c.saveToFile("common_scale.png")


def test_symmetry_dot(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    dot = (30, 40)
    triag.symmetry_dot(dot[0], dot[1])
    c.addObject(shape(triag.to_pixels(), getNextColour()))
    c.addObject(shape([dot], getNextColour()))

    c.saveToFile("symmetry_dot.png")


def test_projection(dots):
    c = canvas()

    triag = NGon(dots)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    triag = NGon(dots)
    triag.projection(1/50, 1/24, 3)
    c.addObject(shape(triag.to_pixels(), getNextColour()))

    c.saveToFile("projection.png")

def test_transformations():
    dots = [(10, 15), (40, 60), (90, 5)]
    test_identical(dots)
    test_local_scaling(dots)
    test_symmetry(dots)
    test_shift(dots)
    test_rotation(dots)
    test_symmetry_diag(dots)
    test_common_scaling(dots)
    test_symmetry_dot(dots)
    test_projection(dots)


def test_all():
    test_circle()
    test_segment()
    test_canvas()
    test_arc_brezenhem()
    test_cutting()
    test_transformations()


if __name__ == "__main__":
    clearPNGs()

    test_all()
    # test_transformations()

    can = canvas()

