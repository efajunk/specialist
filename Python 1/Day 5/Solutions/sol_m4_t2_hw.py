"""
Дана строку. Необходимо посчитать количество вхождений каждого символа.
Пример:
In: Hello, Python1
Out: 
H: 1
e: 1
l: 2
o: 2
,: 1
P: 1
y: 1
t: 1
n: 1
1: 1
 : 1
"""
## V1
print('Первый вариант')
string = input('Enter a string: ')
unique_chars = []
## Сначала формируем алфавит нашей строки
for char in string:
    if char not in unique_chars:
        unique_chars.append(char)
        
for char in unique_chars:    
    print(f'{char}: {string.count(char)}')

## V2
print('Второй вариант') 
result = [[char + ': ', string.count(char)] for char in set(string)]
for lst in result:
    for item in lst:
        print(item, end='')
    print()








