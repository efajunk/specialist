import sys
"""
Файлы

Файлы открываются функцией open( file_name, mode ). Функция возвращает объект.

file_name - [путь до файла]имя файла

mode - режим работы с файлом:

    'r': только чтение (default)
    'w': запись ”с нуля” (содержимое файла будет стерто)
    'x': создать (если файл существует, будет выброшено исключение)
    'a': запись в конец файла
    
У объекта file есть следующие методы:

    read(size) - прочитать содержимое файла размером size байтов/символов
    readline() - прочитать строку и передвинуть указатель на следующую
    readlines() - вернуть список строк
    write() - запись в файл, функция возвращает количество записанных символов
    writelines() - запись в файл списка строк

! Файл закрывается методом close().

!! Рекомендуется использовать конструкцию with ... as ...:
   так как он закрывает файл автоматически, после отработки блока with ... as
"""

## Пример 1
# f = open('C:\\Course\\file4test.txt', 'w', encoding='utf-8')
# for _ in range(10):
#     f.write('5 ')
#     f.write('Hello world!\n')
# f.writelines(['Вторая\n', 'строка'])
# f.close()
# 
# ## Менеджер контекста закрывает файл сам
# with open('C:\\Course\\file4test.txt', encoding='utf-8') as input_file:
#     for line in input_file.readlines():
#         print(line, end='')
# 
# print()
# print('done')
# 
## Считываем без менеджера контекста
file = open('C:\\Course\\file4test.txt', 'r', encoding='utf-8')
while res := file.readline():
    print(res, end='')
print()
file.close()

# # ## Используем функцию print с файловым идентификатором
file_out = open('C:\\Course\\examples_file.txt', 'a')
print('Hello Python', file=file_out)
print(5, 8, 8.1, file=file_out)

## Используем значение аргумента file по умолчанию
print(f'Our version is {sys.version}')

file_out.write('this is just a text\n')
print(*[4, 8, 9, 12], file=file_out)
file_out.close()


path = 'C:\\Course\\examples_file.txt'
# # ## Пример работы менеджера контекста
with open(path) as read_file:
    for line in read_file.readlines():
        print(line, end='')
print()



