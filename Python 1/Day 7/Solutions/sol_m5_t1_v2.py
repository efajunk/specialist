"""
Даны координаты трех точек(x1, y1, x2, y2, x3, y3), которые >= 0.
Нужно написать Написать 3 функции:
Первая функция определяет - можно ли построить треугольник по координатам.
Вторая функция вычисляет площадь треугольника.
Третья функция определяет - является ли треугольник прямоугольным.
"""
import sys

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    '''Calculating the length of a straight line'''
    c = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(c, 2)

def triangle(a: float, b: float, c: float) -> str:
    '''Can you build a triangle??'''
    if a + b > c and a + c > b and b + c > a:
        return "По данным координатам можно построить треугольник"
    return "По данным координатам нельзя построить треугольник"

def s_triangle(a: float, b: float, c: float) -> float:
    '''Calculating the area of a triangle'''
    p = (a + b + c) / 2  # Полупериметр 
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return round(s, 2)

def right_triangle(a: float, b: float, c: float) -> str:
    '''Right triangle?'''
    temp = [a, b, c]
    temp.sort()
    a, b, c = temp
    if a * a + b * b == c * c:
        return("Данный треугольник - прямоугольный")
    return("Данный треугольник не является прямоугольным")

def in_out():
    ''' In and Out function for testing '''
    x1, y1 = [float(i) for i in input("Введите координаты 1 точки: ").split()]
    x2, y2 = [float(i) for i in input("Введите координаты 2 точки: ").split()]
    x3, y3 = [float(i) for i in input("Введите координаты 3 точки: ").split()]

    distance_1_2 = distance(x1, y1, x2, y2)
    distance_2_3 = distance(x2, y2, x3, y3)
    distance_1_3 = distance(x1, y1, x3, y3)

    if triangle(distance_1_2, distance_2_3, distance_1_3) == 'По данным координатам нельзя построить треугольник':
        print("К сожалению, треугольник построить не получится. \n Дальнейшее выполнение программы не имеет смымсла.")
        sys.exit()

    ## Для удобства восприятия вывел длины сторон
    print("Сторона А треугольника = ", distance_1_2)
    print("Сторона B треугольника = ", distance_2_3)
    print("Сторона C треугольника = ", distance_1_3)

    print(triangle(distance_1_2, distance_2_3, distance_1_3))
    print(right_triangle(distance_1_2, distance_2_3, distance_1_3))
    print(f"Площадь треугольника равна = {s_triangle(distance_1_2, distance_2_3, distance_1_3)}")


if __name__ == '__main__':
    in_out()