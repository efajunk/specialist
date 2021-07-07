'''
Задача №3
Дано натуральное число N. Если число N двузначное,
то найти сумму цифр числа. Если число N трехзначное,
то найти произведение ненулевых цифр числа
'''
number_str = input('Введите двузначное число или трехзначное: ')
number = int(number_str)

if len(number_str) == 2 and number > 9:
	print(f'Сумма цифр числа {number} равна: {number // 10 + number % 10}')
elif len(number_str) == 3:
    first_place = number // 100 % 10
    second_place = number // 10 % 10
    thrid_place = number % 10

    if first_place == 0:
        first_place = 1
    if second_place == 0:
        second_place = 1
    if third_place == 0:
        third_place = 1
    print(f'Произведение цирф числа {number} равна: {(first_place) * (second_place) * (thrid_place)}')          
else:
	print(f'Число {number} не двузначное или трехзначное или введены нули')
