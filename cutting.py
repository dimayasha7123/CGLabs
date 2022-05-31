def sutherland(rectX1: int, rectY1: int, rectX2: int, rectY2: int, cutting: list) -> list:
    output = []
    for pixel in cutting:
        if rectX1 <= pixel[0] <= rectX2 and rectY1 <= pixel[1] <= rectY2:
            output.append(pixel)
    return output


# далее идет бесполезный код, похожий на правду, но я сдал то, что выше . . .
def get_code(param, rect):
    pass


def is_visible(bar, rect):
    pass


def log_prod(code1, code2):
    p = 0
    for i in range(4):
        p += code1[i] & code2[i]

    return p


def is_visible(bar, rect):
    """Видимость - 0 = невидимый
                   1 = видимый
                   2 = частично видимый"""
    # вычисление кодов концевых точек отрезка
    s1 = sum(get_code(bar[0], rect))
    s2 = sum(get_code(bar[1], rect))

    # предположим, что отрезок частично видим
    vis = 2

    # проверка полной видимости отрезка
    if not s1 and not s2:
        vis = 1
    else:
        # проверка тривиальной невидимости отрезка
        l = log_prod(get_code(bar[0], rect), get_code(bar[1], rect))
        if l != 0:
            vis = 0

    return vis


def cohen_sutherland(bar, rect, win):
    # инициализация флага
    flag = 1  # общего положения
    t = 1

    # проверка вертикальности и горизонтальности отрезка
    if bar[1][0] - bar[0][0] == 0:
        flag = -1  # вертикальный отрезок
    else:
        # вычисление наклона
        t = (bar[1][1] - bar[0][1]) / (bar[1][0] - bar[0][0])
        if t == 0:
            flag = 0  # горизонтальный

    # для каждой стороны окна
    for i in range(4):
        vis = is_visible(bar, rect)
        if vis == 1:
            win.scene.addLine(bar[0][0], bar[0][1], bar[1][0], bar[1][1], win.pen)
            return
        elif not vis:
            return

        # проверка пересечения отрезка и стороны окна
        code1 = get_code(bar[0], rect)
        code2 = get_code(bar[1], rect)

        if code1[i] == code2[i]:
            continue

        # проверка нахождения Р1 вне окна; если Р1 внутри окна, то Р2 и Р1 поменять местами
        if not code1[i]:
            bar[0], bar[1] = bar[1], bar[0]

        # поиск пересечений отрезка со сторонами окна
        # контроль вертикальности отрезка
        if flag != -1:
            if i < 2:
                bar[0][1] = t * (rect[i] - bar[0][0]) + bar[0][1]
                bar[0][0] = rect[i]
                continue
            else:
                bar[0][0] = (1 / t) * (rect[i] - bar[0][1]) + bar[0][0]

        bar[0][1] = rect[i]
    win.scene.addLine(bar[0][0], bar[0][1], bar[1][0], bar[1][1], win.pen)
