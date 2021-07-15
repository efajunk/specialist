def is_triangle(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
    if (y3 - y1) * (x2 - x1) == (x3 - x1) * (y2 - y1):
        return 'Не треугольник'
    return 'Треугольник'


def triangle_area(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
    return 0.5 * abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))


def right_triangle(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
    d1 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    d2 = (x3 - x1) ** 2 + (y3 - y1) ** 2
    d3 = (x3 - x2) ** 2 + (y3 - y2) ** 2
    if d1 == d2 + d3 or d2 == d1 + d3 or d3 == d1 + d2:
        return 'Прямоугольный треугольник'
    return 'Не прямоугольный треугольник'


x1, y1, x2, y2, x3, y3 = [float(i) for i in input('Укажите координаты треугольника: ').split()]
check = is_triangle(x1, y1, x2, y2, x3, y3)
print(check)
if check.startswith('Тр'):
    area = triangle_area(x1, y1, x2, y2, x3, y3)
    print('Площадь: ', area)
    check2 = right_triangle (x1, y1, x2, y2, x3, y3)
    print('Вид треугольника: ',check2)
