import math
from circle_brezenhem import circle_brezenhem


def triangle_area_2(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def clockwise(x1, y1, x2, y2, x3, y3):
    return triangle_area_2(x1, y1, x2, y2, x3, y3) < 0


def counter_clockwise(x1, y1, x2, y2, x3, y3):
    return triangle_area_2(x1, y1, x2, y2, x3, y3) > 0


def arc_brezenhem(x0, y0, r, angF, angS):
    print(f'First angle:  {angF}')
    print(f'Second angle: {angS}')
    xF, xS = 1, 1
    if angF <= 90 or angF >= 270:
        xF = 1
    else:
        xF = -1
    if angS <= 90 or angS >= 270:
        xS = 1
    else:
        xS = -1
    angF *= math.pi / 180
    angS *= math.pi / 180
    yF = math.tan(angF) * xF
    yS = math.tan(angS) * xS
    print(f'First:  {xF, yF}')
    print(f'Second: {xS, yS}')

    dotF = (1, 1)
    print(clockwise(x0, y0, xF, yF, dotF[0], dotF[1]))
    print(counter_clockwise(x0, y0, xF, yF, dotF[0], dotF[1]))
    print(clockwise(x0, y0, xS, yS, dotF[0], dotF[1]))
    print(counter_clockwise(x0, y0, xS, yS, dotF[0], dotF[1]))

    from_circle = circle_brezenhem(x0, y0, r)
    output = []
    for i in range(0, len(from_circle)):
        if counter_clockwise(x0, y0, xF, yF, from_circle[i][0], from_circle[i][1]) and \
                clockwise(x0, y0, xS, yS, from_circle[i][0], from_circle[i][1]):
            output.append((from_circle[i][0], from_circle[i][1]))

    return output
