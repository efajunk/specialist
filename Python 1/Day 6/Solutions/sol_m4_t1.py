"""
Написать 3 функции и оформить решение в виде модуля.
Дан участок земли прямоугольной формы.
Нужно посчитать стоимость самой земли и забора по периметру.

Первая функция принимает в качестве аргументов длину и ширину участка.
Возвращает периметр и площадь.

Вторая функция принимает в качестве аргументов периметр и стоимость погонного метра забора.
Возвращает итоговую сумму.

Третья функция принимает в качестве аргументов площадь и стоимость одного квадратного метра земли.
Возвращает итоговую сумму.
"""
## V1
def zemlemer(a: float, b: float) -> tuple:
    '''square and perimetr'''
    square = a * b
    perimetr = (a + b) * 2
    return round(square, 2), round(perimetr, 2)

def stroitel(P: float, MP_cost: float) -> float:
    ''' fence cost'''
    zabor_price = P * MP_cost
    return zabor_price

def rieltor(S: float, SQM_cost: float) -> float:
    ''' land price '''
    zabor_price = S * SQM_cost
    return zabor_price

length, width = [float(i) for i in input('Enter length and width: ').split()]
fence_price = float(input('Введите стоимость погонного метра ограды: '))
land_price = float(input('Введите стоимость кв.м. земли: '))

fence = stroitel(zemlemer(length, width)[1], fence_price)
print(f'{fence = }')

land = rieltor(zemlemer(length, width)[0], land_price)
print(f'{land = }')


## V2
def per_and_area(lenght: int, width: int) -> int:
    perimeter = (lenght + width) * 2
    area = width * lenght
    return perimeter, area
    
def fence_cost(perimeter: int, price: int) -> int:
    final_cost = perimeter * price
    return final_cost
    
def ground_cost(area: int, price: int) -> int:
    final_cost = area * price
    return final_cost
    
g_cost = int(input('Введите стоимость земли: '))
f_cost = int(input('Введите стоимость забора: '))
lenght = int(input('Введите длину участка: '))
width = int(input('Введите ширину участка: '))

per, area = per_and_area(lenght, width)
print(f'Стоимость земли: {ground_cost(area, g_cost)}')
print(f'Стоимость забора: {fence_cost(per, f_cost)}')


## V3
def ps(l, s):
    return 2 * (l + s), l * s

def sum_metr(per, amount):
    return per * amount

def sum_zem(s, amount_m_zem):
    return s * amount_m_zem

l = int(input('Введите длину уч-ка:'))
s = int(input('Введите ширину уч-ка:'))
amount = int(input('Введите стоимость погонного метра:'))
amount_zem = int(input('Введите стоимость метра земли:'))
per, sq = ps(l,s)
sum_zabora = sum_metr(per, amount)
sum_zem = sum_zem(sq, amount_zem)
print(f'Периметр = {per}, площадь = {sq} стоимость забора = {sum_zabora}, '
      f'стоимость земли = {sum_zem}')