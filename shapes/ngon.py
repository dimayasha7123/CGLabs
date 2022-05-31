from shapes.segment_brezenhem import segment_brezenhem
import numpy as np


class NGon:
    def __init__(self, dots):
        self.matr = np.empty((len(dots), 2))
        for i in range(len(dots)):
            self.matr[i][0] = dots[i][0]
            self.matr[i][1] = dots[i][1]

    def to_pixels(self):
        matr = self.matr.astype(int)
        output = segment_brezenhem(
            matr[0][0],
            matr[0][1],
            matr[len(matr) - 1][0],
            matr[len(matr) - 1][1]
        )
        for i in range(len(matr) - 1):
            output.extend(segment_brezenhem(
                matr[i][0],
                matr[i][1],
                matr[i + 1][0],
                matr[i + 1][1]
            ))
        return output

    # вспомогательное преобразование (перемножает матрицы)
    def abstacrt_trans(self, matr):
        self.matr = np.matmul(self.matr, matr)

    # тождественное преобразование
    def identical_trans(self, dots):
        pass

    # локальное масштабирование
    def scaling_trans(self, n):
        m = np.array([[1, 0], [0, 1]])
        m *= n
        self.abstacrt_trans(m)

    # симметрию относительно OX
    def symmetry_x(self):
        m = np.array([[1, 0], [0, -1]])
        self.abstacrt_trans(m)

    # симметрию относительно OY
    def symmetry_y(self):
        m = np.array([[-1, 0], [0, 1]])
        self.abstacrt_trans(m)

    # симметрия относительная начала координат
    def symmetry(self):
        m = np.array([[-1, 0], [0, -1]])
        self.abstacrt_trans(m)

    # сдвиг вдоль оси OX пропорционально координате y
    def shift_x(self, s):
        pass

    # сдвиг вдоль оси OY пропорционально координате x
    def shift_y(self, s):
        pass

# 1.	- тождественное преобразование,
# 2.	+ локальное масштабирование,
# 3.	+ симметрию относительно осей координат,
# 4.	+ симметрию относительно начала координат,
# 5.	- сдвиг вдоль оси ОХ пропорционально координате у,
# 6.	- сдвиг вдоль оси ОУ пропорционально координате х,
# 7.	- поворот на заданный угол вокруг начала системы координат,
# 8.	- симметрию относительно прямых у=х и у=-х,
# 9.	- перемещение (параллельный перенос) на заданный вектор,
# 10.	- проецирование в однородных координатах,
# 11.	- общее масштабирование.

# С помощью простейших преобразований реализовать
# 1.	- поворот относительно произвольной точки и
# 2.	- симметрию относительно произвольной прямой.
