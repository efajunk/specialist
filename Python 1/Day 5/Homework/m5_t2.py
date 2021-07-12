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
import string

size = int(input('Введите размер шахматной доски от 0 до 20: '))

alpha = string.ascii_lowercase

# digits = [i for i in range(size, 0, -1)]

for i in range(size, 0, -1):
    for j in range(size):
        print(alpha[j], i, sep='', end=' ')
#         print(alpha[j], digits[i], sep='', end=' ')
    print('')
    
##V2

size = int(input('Введите размер шахматной доски от 0 до 20: '))

alpha = string.ascii_lowercase

for i in range(size, 0, -1):
    for j in range(size):
#        print(alpha[j], i, sep='', end=' ')
        print(f'{alpha[j] + str(i): <3}', end=' ')
    print('')
