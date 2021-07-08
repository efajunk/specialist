"""
Дана строка из двух слов. Поменяйте эти слова местами.
Пример:
In: Hello Python
Out: Python Hello
"""
string = input('Введите два слова: ')
index_of_space = string.index(' ')
first_word = string[:index_of_space]
second_word = string[index_of_space + 1:]

print(f'{second_word} {first_word}')

