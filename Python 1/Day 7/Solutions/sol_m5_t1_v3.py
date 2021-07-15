"""
Даны координаты трех точек(x1, y1, x2, y2, x3, y3), которые >= 0.
Нужно написать Написать 3 функции:
Первая функция определяет - можно ли построить треугольник по координатам.
Вторая функция вычисляет площадь треугольника.
Третья функция определяет - является ли треугольник прямоугольным.
"""
import math


def lenght_side(x: tuple, y: tuple) -> tuple:
    ''' Only three points '''
    c1 = round(((x[2] - x[0]) ** 2 + (y[2] - y[0]) ** 2) ** 0.5, 3)
    c2 = round(((x[2] - x[1]) ** 2 + (y[2] - y[1]) ** 2) ** 0.5, 3)
    c3 = round(((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2) ** 0.5, 3)
    c = [c1, c2, c3]
    if c[0] + c[1] == c[2] or c[0] + c[2] == c[1] or c[1] + c[2] == c[0]:
        triangle = 0
    else:
        triangle = 1
    return c, triangle


def square_triangle(lenght_sides: tuple) -> float:
    pol_per = (sum(lenght_sides)) / 2
    square_triangle = round(((pol_per
                                * (pol_per - lenght_sides[0])
                                * (pol_per - lenght_sides[1])
                                * (pol_per - lenght_sides[2])) ** 0.5), 3)
    return square_triangle


def triangle_rectan(lenght_sides: tuple, square: float) -> bool:
    if (square == (lenght_sides[0] * lenght_sides[1]) / 2  or
        square == (lenght_sides[1] * lenght_sides[0]) / 2  or
        square == (lenght_sides[1] * lenght_sides[2]) / 2):
        return 1
    return 0


x1, y1 = [float(i) for i in input("Введите координаты первой точки (х1, у1) ").split()]
x2, y2 = [float(i) for i in input("Введите координаты второй точки (x2, y2) ").split()]
x3, y3 = [float(i) for i in input("Введите координаты третьей точки (х3, у3) ").split()]
x = (x1, x2, x3)
y = (y1, y2, y3)
lenght_sides = lenght_side(x, y)[0]
triangle = lenght_side(x, y)[1]
if triangle == 1:
    square = square_triangle(lenght_sides)
    rectan = triangle_rectan(lenght_sides, square)
    print("Треугольник по введенным координатам построить можно.")
    print("Площадь треугольника =", "{0:.2f}".format(square))
    if rectan == 1:
        print("Треугольник прямоугольный")
else:
    print("Треугольник по введенным координатам построить нельзя")
