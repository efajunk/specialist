# # Функция полноправный объект в языке Python:
# # • может быть создан во время выполнения;
# # • может быть присвоен переменной или полю структуры данных;
# # • может быть передан функции в качестве аргумента;
# # • может быть возвращен функцией в качестве результата.

def func(text:str) -> str:
    return text.upper() + '!'
# 
# print(func('привет'))
# 
bar = func
# print(type(bar), bar) 
# print(bar('пока'))
# 
# # Можно удалить func, но bar будет вызываться
del func
###print(func('textest')) ## Out -> Error
# # # 
# print(bar('Я работаю'))
# print(bar.__name__)
# 
# # 
# # ## Можно хранить функции в структурах данных
# funcs = [bar, str.lower, str.capitalize]
# print(funcs)
# # # # 
# # # # ## Доступ в функциям, хранящимся внутри списка
# for function in funcs:
#      print(function.__name__, '->', function('проверка Работы'))
# 
# ## Вызов функции как элемента списка по индексу 
# print(funcs[0]('первая функция'))

# dict_ex = {1: str.lower,
#            2: str.upper,
#            3: int,
#            4: float}
# 
# enter = int(input('Введите номер функции: '))
# f = dict_ex[enter]
# print(f('hello'))
# if enter < 4:
#     f = dict_ex[enter + 1]
#     print(f('123'))


# ## Передача функции в другую функцию
# def greet(func_name):
#     greeting = func_name('Программа на Python')
#     print(greeting)
# 
# ## Вызов функции greet с аргументом - функцией bar 
# greet(bar)
# # # # 
# def imp_func(text):
#      return text.lower() + '. Done!'
# 
# ## Вызов функции greet с аргументом - функцией imp_func
# greet(imp_func)

# ## Функции более высокого порядка(higher-order functions)
# ## map, filter, reduce
# print(map(bar, ['hello', 'hi', 'привет']))
# 
# print(list(map(bar, ['hello', 'hi', 'привет'])))
# 
# print(tuple(map(int, input('Enter numbers: ').split())))
# 
# a, b = map(int, input('Enter numbers again: ').split())
# print(f'{a = }, {b = }')
# # # 
# def condition(text):
#      return len(text) > 3
# # ## Включаем элемент в итоговый список, если результат работы
# # ## функции condition True
# print(list(filter(condition, ['hello', 'hi', 'привет'])))


## Функция reduce
# def add_two(a, b):
#     print(f'{a = }, {b = }')
#     return a + b
# 
# from functools import reduce
# print(reduce(add_two, ['hello', 'hi', 'привет', '5']))


# ## Пример функции zip
# a = list(range(7))
# b = list(range(11, 26))
# c = True, False, True, True, False, False
# d = 'Pythons'
# for item in zip(a, b, c, d):
#     print(f'{item = }')
# 
# 
# print(list(zip(a, b, c, d)))

# ## Вложенные функции
a = 9
def main(text:str):
    a = 5
    def inner_func(text_1:str):
        nonlocal a
        a += 1
        print(locals())
        return text_1.lower() + '...' + f'{a}'
    print(locals()) ## Словарь локальных переменных
    return inner_func(text)

print(main('Привет, Всем '))
print(f'{a = }')
# # print(inner_func('Может работает?')) # Error
# # print(main.inner_func) # Error

