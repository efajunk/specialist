"""
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
"""
# ## V1
# n = int(input("Введите размер доски: "))
# chess_desk = []
# if 0 <= n <= 20:
#     chess_desk = [[(j + i) % 2 for j in range(n)] for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             print(chess_desk[i][j], end=" ")
#         print()
# else:
#     print("Введите верное число, от 0 до 20. Вы ввели:", n)

## V2
# n = int(input("Введите целое число от 0 до 20: "))
# for j in range(n):    
#     for i in range(n):
#         if j % 2 == 0:
#             print(i % 2, end=" ")
#         else:
#             print((i + 1) % 2, end=" ")
#     print()

## V3
# size = int(input("Введите размер шахматной доски: "))
# flag = even_check = 0
# 
# if size % 2 == 0:
#     even_check = 1
#     shift_count = size
# 
# for i in range(size):
#     for j in range(size):
#         if flag == 0:
#             print(0, end=' ')
#             flag = 1
#         else:
#             print(1, end=' ')
#             flag = 0
#     if even_check == 1:
#         if shift_count % 2 == 0:
#             shift_count -= 1
#             flag = 1
#         else:
#             shift_count -= 1
#             flag = 0
#         
#     print('')
    
## V4
# chislo = int(input('Введите число: '))
# result = list()
# result_2 = list()
# for i in range(chislo):
#     if not i % 2:
#         result.append(0)
#         result_2.append(1)
#     else:
#         result.append(1)
#         result_2.append(0)
#         
# for i in range(chislo):               
#     if not i % 2:
#         print(*result)
#     else:
#         print(*result_2)


## V4.1
# chislo = int(input('Введите число: '))
# result = list()
# for i in range(chislo):
#     if not i % 2:
#         result.append(0)
#     else:
#         result.append(1)
#         
# result_2 = [j ^ 1 for j in result]
# 
# for i in range(chislo):               
#     if not i % 2:
#         print(*result)
#     else:
#         print(*result_2)

## V5
n = int(input('Введите размер шахматной доски -> '))
chess_board = [['0' for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if (i + j) % 2:
            chess_board[i][j] = '1'
for string in chess_board:
    print(' '.join(string))











