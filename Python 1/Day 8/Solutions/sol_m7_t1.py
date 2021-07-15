"""
Написать функцию для сложения двух аргументов, в которую нужно
добавить обработку исключений для случаев сложения str с int, float и bool
"""

## V1
# def exception_process(a, b):
#     try:
#         return a + b
#     except TypeError as err:
#         return (f'Ошибка "{err}". Попытка преобразовать данные в строку.\n'
#                 f' Это все, что я могу сделать для вас: {str(a) + str(b)}')
# 
# 
# 
# print(exception_process('aa' , 5))
# print(exception_process('aa' , True))
# print(exception_process('aa' , '5'))
# print(exception_process('aa' , 5.1))
# print(exception_process(7 , 5))
# print(exception_process(8.1 , 5))
# print(exception_process(True , 5))

## V2

def func1(first_arg, second_arg):
    try:
        return sum([first_arg, second_arg])
    except TypeError:
        return('Ошибка ввода. Попытка сложения ' + str(type(first_arg)) +' с ' + str(type(second_arg)))


        
print(func1('aa' , 5))
print(func1('aa' , True))
print(func1('aa' , '5'))
print(func1('aa' , 5.1))
print(func1(7 , 5))
print(func1(8.1 , 5))
print(func1(True , 5))