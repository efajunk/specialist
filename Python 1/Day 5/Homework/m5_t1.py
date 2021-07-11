'''
Задача №1. Шахматная доска
Вход: размер шахматной доски (NxN), где N - число от 0 до 20.
Выход: вывести на экран эту доску, заполняя поля нулями и единицами

Пример:
Вход: 5
Выход:
    0 1 0 1 0
    1 0 1 0 1
    0 1 0 1 0
    1 0 1 0 1
    0 1 0 1 0
'''
size = int(input("Введите размер шахматной доски: "))
flag = 0
even_check = 0

if size % 2 == 0:
    even_check = 1
    shift_count = size

for i in range(size):
    for j in range(size):
        if flag == 0:
            print(0, end=' ')
            flag = 1
        else:
            print(1, end=' ')
            flag = 0
    if even_check == 1:
        if shift_count % 2 == 0:
            shift_count -= 1
            flag = 1
        else:
            shift_count -= 1
            flag = 0
        
    print('')