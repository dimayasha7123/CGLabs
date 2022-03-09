import math

def Sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

# какие есть варианты округлить:
#   отбрасывание дробной части (или к нулю) - int()
#   округление вниз - math.floor()
#   округление вверх - math.ceil()
#   округление математическое - round()


def rounder(roundType, num):
    if roundType == "int":
        return int(num)
    elif roundType == "floor":
        return math.floor(num)
    elif roundType == "ceil":
        return math.ceil(num)
    else:
        return round(num)


def CDA (x1, y1, x2, y2, roundType = "math"):
    length = max(abs(x2 - x1), abs(y2 - y1))
    dx = (x2 - x1) / length
    dy = (y2 - y1) / length
    x = x1 + 0.5 * Sign(dx)
    y = y1 + 0.5 * Sign(dy)
    output = []
    for i in range(0, length):
        output.append((rounder(roundType, x), rounder(roundType, y)))
        x = x + dx
        y = y + dy
    return output