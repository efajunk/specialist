# Задача №4
"""
Вход:
    расстояние(50 - 10000 км),
    расход в литрах (5-25 литров) на 100 км и
    стоимость бензина(константа) = 52 руб
    
Математические операции: - + * /

Выход: стоимость поездки в рублях
"""

## V1
dist = int(input('Введите расстояние (от 50 до 10000 км)-> '))
pet = float(input('Введите расход бензина в литрах (от 5 до 25) на 100 км -> '))
PRICE = 52 #стоимость бензина
cost = (pet * PRICE) / 100 * dist #стоимость поездки в рублях
print('Cтоимость Вашей поездки составила -> ', round(cost, 2), ' руб.')


## V2
PRICE = 52
distance = float(input('Введите расстояние поездки в км (от 50 до 10000) : '))
liter_per_hundred = float(input('Введите расход топлива л/100 км (от 5 до 25) : '))
cost = distance / 100 * liter_per_hundred * PRICE
print('Стоимость поездки составит ', round(cost, 2), 'руб.')

## V3
distance = int(input('Введите расстояние: '))
consumption = int(input('Введите расход на 100 км: '))
PRICE = 52
print("Result:", distance / 100 * consumption * PRICE)













