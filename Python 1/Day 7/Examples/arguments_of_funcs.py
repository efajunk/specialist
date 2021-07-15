## *args = кортеж всех позиционные аргументов
## **kwargs - словарь всех именованных аргументов
# def func(*args, **kwargs):
#     print(f'{args = }')
#     print(f'{kwargs = }')

# print('****** First call ********')
# func(8, 2, 1, 100)
# # 
# print('****** Second call *******')
# func(4, 6, teacher='VSH', students='all')


## В этом примере name - это именованный аргумент
def func_1(*args, name):
    print(f'{args = }')
    print(f'{name = }')
    name += '5'
    print(f'{name = }')
    if args:
        for item in args:
            print(item * 2)

func_1(2, 4.1, 5, 0, 8, 7, 0, 4, name='smith')
# func_1('a', 'b', 'c', 'd','hello', 'python', name='students')


# def example(a, b, c, d=1):
#     print(f'{d = }')
#     return a * b + c * d
# # 
# print(example(2, 5, d=5, c=3))
# 
# # ## Используем значение по умолчанию для d
# print(example(2, 5, 5))
# # 
# # ## Передаем значение 100 для d
# print(example(8, 2, 1, 100))
# 


# # a и b - только позиционные
# # c и d - и позиционные и именованные
# # e и f - только именованные
# # до символа / только позиционные
# # после символа * только именованные
# def big(a, b, /, c, d, *, e, f):
#     return a + b + c + d + e + f
# 
# 
# 
# print(big(4, 5, 7, 8, f=9, e=10))
# print(big(4, 5, 7, d=8, f=9, e=10))
# print(big(4, 5, c=7, d=8, f=9, e=10))
## Errors
# print(big(4, b=5, c=7, d=8, f=9, e=10))
# print(big(4, 5, 7, 8, 9, f=10))

# def must_one(arg1, *other):
#     print(f'{arg1 = }')
#     if other:
#         print(*other)
#     return other 
# 
# #print(must_one()) ## Out -> Error
# print(must_one(1, 45, 56, 'hello', 'python'))




















