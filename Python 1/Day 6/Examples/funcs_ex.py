def func_1():
    n = int(input('Введите количество бутылок -> '))
     
    ending_word = ('ка', 'ок', 'ки')
    n_1 = n % 100

    if n_1 in (11, 12, 13, 14):
        e_w = ending_word[1]
    else:
        n_1 %= 10
        if n_1 in (2, 3, 4):
            e_w = ending_word[2]
        elif n_1 == 1:
            e_w = ending_word[0]
        else:
            e_w = ending_word[1]
            
    print(f'{n} бутыл{e_w}')

# func_1()

def func_2():
    n = int(input('Введите количество бутылок -> '))
     
    ending_word = ('ка', 'ок', 'ки')
    n_1 = n % 100

    if n_1 in (11, 12, 13, 14):
        e_w = ending_word[1]
    else:
        n_1 %= 10
        if n_1 in (2, 3, 4):
            e_w = ending_word[2]
        elif n_1 == 1:
            e_w = ending_word[0]
        else:
            e_w = ending_word[1]
            
    return f'{n} бутыл{e_w}'

# result = func_2()
# print(result)


## Области видимости
## Local -> Enclosed -> Global -> Builtin

# def func_3(n):
#     ending_word = ('ка', 'ок', 'ки')
#     n_1 = n % 100
#     if n_1 in (11, 12, 13, 14):
#         e_w = ending_word[1]
#     else:
#         n_1 %= 10
#         if n_1 in (2, 3, 4):
#             e_w = ending_word[2]
#         elif n_1 == 1:
#             e_w = ending_word[0]
#         else:
#             e_w = ending_word[1]
        ## Словарь локальных переменных
# #     print(locals())
#     return f'{n} бутыл{e_w}'

# number = int(input('Введите количество бутылок -> '))
# res = func_3(number)
# print(res)

##**************** START *******************##
def func_4(n, word):
    ending_word = ('ка', 'ок', 'ки')
    n_1 = n % 100
    if n_1 in (11, 12, 13, 14):
        e_w = ending_word[1]
    else:
        n_1 %= 10
        if n_1 in (2, 3, 4):
            e_w = ending_word[2]
        elif n_1 == 1:
            e_w = ending_word[0]
        else:
            e_w = ending_word[1]
    return word.upper(), e_w.upper()
##****************** END *******************##



# num = int(input('Введите количество бутылок -> '))

###Результат вызыва функции - кортеж 
# one_param = func_4(num, 'бутыл')
# print(one_param[0], one_param[1], sep='')
# 
# base, endings = func_4(num, 'бутыл')
# print(f'{num} {base}{endings}')


for i in [4, 9, 11, 111, 115]:
    print(f'{i} БУТЫЛ{func_4(i, "бутыл")[1]}')


## Функция со значением по умолчанию
def func_5(n: int, word='бутыл') -> str:
    '''Right endings for bottles and others '''
    
    ending_word = ('ка', 'ок', 'ки')
    n_1 = n % 100
    if n_1 in (11, 12, 13, 14):
        e_w = ending_word[1]
    else:
        n_1 %= 10
        if n_1 in (2, 3, 4):
            e_w = ending_word[2]
        elif n_1 == 1:
            e_w = ending_word[0]
        else:
            e_w = ending_word[1]
    return word + e_w


number = int(input('Введите количество бутылок -> '))
answer = func_5(number)
print(f'{number} {answer}')

answer_1 = func_5(number, 'бан')
print(f'{number} {answer_1}')









