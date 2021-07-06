#### Условный оператор if

## Шаблон
# # if условие верно(True): 
# #     Блок инструкций 1
# #     Выражение_1
# #     Выражение_2 
# # elif условие верно:
# #     Блок инструкций 2
# # elif условие верно:
# #     Блок инструкций 3
# # elif условие верно:
# #     Блок инструкций 4
# # elif условие верно:
# #     Блок инструкций 5
# # else:
# #     Блок инструкций 6

## Пример 1
# string_one = 'hello'
# string_second = 'python'
# if len(string_one) < len(string_second):
#     print('string_second is bigger')
# print('Проверка прошла')

## Пример 2
# data = int(input('Enter value: '))
# if data > 0:
#     print(f'Число {data} положительное')
# elif data < 0:
#     print(f'Число {data} отрицательное')
# else:
#     print(f'Это число {data}')


## Операции сравнения
# == равно
# != не равно
# <  меньше
# <= меньше или равно
# >  больше 
# >= больше или равно
# in входит в объект
# not in не входит в объект
# string = 'Hello'
# print('e' in string)
# print('a' in string)
# print('e' not in string)
# print('a' not in string)

## Пустая переменная
# data_1 = None ## Создание просто имени
# print(type(data_1)) ## Out -> NoneType
# 
# data = '' # Пустая строка  Falsy value

# Если data равно 0 или пустой строке, то значение выражения - False
# Если data не равно 0 или пустой строке, то значение выражения - True
# if data: 
#     print('В строке есть значения')
# else:
#     print('Строка пустая')
# #

# 
# n = int(input('Enter "n" number(1-1000): '))
# m = int(input('Enter "m" number(1-1000): '))
#  
# #### Логические операторы and, or, not
# ## Логическое 'И'
# if n > 0 and m < 100: # True and True
#     print('Первая проверка пройдена')
# #     
# ##Логическое 'ИЛИ'. Ленивый оператор
# if n > 0 or m < 100:  # True or False -> True; False or True -> True
#     print('Вторая проверка пройдена')

a, b, c = input("Enter a, b, c: ").split()
# ## Множественное присваивание
a, b, c = int(a), int(b), int(c)
if a > 1 or b > 0 or c < 2:
    print("work")


## Тернарный оператор
a = 100
b = 99
## Старая версия
if a > b:
    result = a
else:
    result = b
    
## Новая версия
result = a if a > b else b
print(f'{result = }')
print('a больше b') if a < b else print('a не больше b')



















