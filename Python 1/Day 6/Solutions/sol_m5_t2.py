'''
Задача №3
Вход: размер шахматной доски, от 0 до 20
Выход: вывести на экран эту доску с названиями полей.
Пример:
In: 4
Out:
a4 b4 c4 d4
a3 b3 c3 d3
a2 b2 c2 d2
a1 b1 c1 d1
'''
## V1
import string
# 
# n = int(input('Введите размер шахматной доски - > '))
# chess_board = [[' ' for i in range(n)] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         chess_board[i][j] = string.ascii_letters[j] + str(n - i)
# for string in chess_board:
#     print(' '.join(string))
    

## V1.1
# n = int(input('Введите размер шахматной доски - > '))
# chess_board = [[0] * n for i in range(n)]
# 
# for i in range(n):
#     for j in range(n):
#         chess_board[i][j] = string.ascii_letters[j] + str(n - i)
#         
# for string in chess_board:
#     print(*string, sep=' ')

    
## V2
import string

size = int(input('Введите размер шахматной доски от 0 до 20: '))

alpha = string.ascii_lowercase

for i in range(size, 0, -1):
    for j in range(size):
        print(f'{alpha[j] + str(i): <3s}', sep='', end=' ')
    print('')
    
    
## V3
# import sys
# import string
# 
# n = int(input("Введите размер доски: "))
# chess_desk = []
# alphabet = string.ascii_uppercase
# 
# if n <= 20:
#     chess_desk = list(range(1, n + 1))
# else:
#     print("Введите верное число, от 0 до 20. Вы ввели:", n)
#     sys.exit()
# for i in range(n - 1, -1, -1):
#     for j in range(n):
#         print(f'{alphabet[j] + str(chess_desk[i]): <3s}', end=' ')
#     print()
    
    
## V4
# chislo = int(input('Введите число:'))
# lst = string.ascii_lowercase[:chislo]
# 
# for i in range(chislo):
#     for char in lst:
#         print(f'{char}{chislo - i}', end = ' ')
#     print()

    
    
    
    