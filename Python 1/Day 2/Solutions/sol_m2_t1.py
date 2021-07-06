'''
Задача №1
Найти среди заданных чисел a, b, c, d
количество чисел, равных нулю
'''
## V1
a, b, c, d = input('Введите четыре числа разделённые пробелом: ').split()
a, b, c, d = int(a), int(b), int(c) ,int(d)

count_of_zero = 0

if a == 0:
    count_of_zero += 1
if b == 0:
    count_of_zero += 1
if c == 0:
    count_of_zero += 1
if d == 0:
    count_of_zero += 1
    
if count_of_zero:
    print(f'Количество чисел равных нулю: {count_of_zero}')
else
    print('Чисел равных нулю нет')

    
 
## V2 
result = (a == 0) + (b == 0) + (c == 0) + (d == 0)
print(f'{result = }')

## V3
count = 0
if not a:
    count += 1
if not b:
    count += 1
if not c:
    count += 1
if not d:
    count += 1
print(f'{count = }')    
    
    
    