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

endings = ['ок', 'ка', 'ки']
bottles_count = int(input('Введите количество бутылок: '))
bottles_find = bottles_count % 100

if 21 > bottles_find > 4 or 4 < (bottles_find % 10) < 10:
    print(f'{bottles_count} {bottle_word}{endings[0]}')
elif bottles_count % 10 == 1:
    print(f'{bottles_count} {bottle_word}{endings[1]}')
else:
    print(f'{bottles_count} {bottle_word}{endings[2]}')

def func_3(bottles_count):
    endings = ['ок', 'ка', 'ки']
    bottle_word = 'бутыл'
    bottles_find = bottles_count % 100

    if 21 > bottles_find > 4 or 4 < (bottles_find % 10) < 10:
        return f'{bottles_count} {bottle_word}{endings[0]}'
    elif bottles_count % 10 == 1:
        return f'{bottles_count} {bottle_word}{endings[1]}'
    else:
        return f'{bottles_count} {bottle_word}{endings[2]}'

count = int(input('Введите количество бутылок: '))
result = func_3(count)
print(result)
