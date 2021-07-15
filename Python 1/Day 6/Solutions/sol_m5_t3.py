"""
Задаем количество бутылок от 0 до 200.
Нужно вернуть количество и слово бутыл<?> с правильным окончанием.
Пример :
In: 5
Out: 5 бутылок
    
In: 1
Out: 1 бутылка
    
In: 22
Out: 22 бутылки
"""
## V1
# n = int(input('Введите количество бутылок -> '))
#  
# ending_word = ('ка', 'ок', 'ки')
# n_1 = n % 100
# 
# if n_1 in (11, 12, 13, 14):
#     e_w = ending_word[1]
# else:
#     n_1 %= 10
#     if n_1 in (2, 3, 4):
#         e_w = ending_word[2]
#     elif n_1 == 1:
#         e_w = ending_word[0]
#     else:
#         e_w = ending_word[1]
#         
# print(f'{n} бутыл{e_w}')


## V2
# number = int(input("Введите количество бутылок: "))
# n = number % 100
# 
# if (n == 0 or
#     20 >= n > 4 or
#     n % 10 >= 5 or
#     n % 10 == 0):
#     suf = "ок"
#     
# elif (n == 1 or
#      n % 10 == 1):
#     suf = "ка"
#     
# elif (4 >= n > 1 or
#       (2 <= n % 10 <= 4 and n > 20)):
#     suf = "ки"
#     
# print(f"{number} бутыл{suf}")


## V3
# number = input("Введите количество бутылок: ")
# a = [int(i) for i in number]
# if len(a) < 2:
#     a.insert(0, 0)
# if a[-1] == 1 and a[-2] != 1:
#     print(f'{number} бутылка')
# elif 1 < a[-1] < 5 and a[-2] != 1:
#     print(f'{number} бутылки')
# else:
#     print(f'{number} бутылок')


## V4
i = int(input('Введите количество бутылок: '))

if i < 0:
    print('Ошибка')
elif i % 10 == 1 and i % 100 != 11: 
    print(i, 'бутылка')
elif i % 10 >= 2 and i % 10 <= 4 and (i % 100 < 10 or i % 100 > 20):  
    print(i, 'бутылки')
else:
    print(i, 'бутылок')
    
