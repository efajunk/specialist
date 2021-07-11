from pprint import pprint

## Dictionaries - Словари(структуры данных для пар "ключ-значение")
## {key: value}
dict_n = {1: [3, 1, 4],
          2: 4.1,
          3:'value',
          (4, 5): True,
          'first': 6}
# print(dict_n)
## Функция hash может быть применима только к unmutable объектам
# print(hash((2, 5)))
# print(hash('name'))
# print(hash('surname'))
# print(hash(2))
# print(hash(9.5))

## Доступ по ключу
dict_n[3] = 'changed_value'
dict_n['first'] = 99
# print(dict_n)
# print(dict_n['first'])
##print(dict_n['second']) ## KeyError нет такого ключа

## Создание новой пары: ключ-значение
dict_n['second'] = 12
# print(dict_n)

## name, surname - это ключи(строки)
# dict_a = dict(name = (2, 5), surname = '2')
# print(dict_a)
# dict_c = dict(a1 = 4, a9 = '2')
# print(dict_c)
# 
# # ##Генератор словарей
# dict_m = {str(i): i * 2 for i in range(10)}
# pprint(dict_m) ## Красивый вывод словаря
# print(len(dict_m))

## Встроенные функции для словарей
# print('Builtins methods for dictionaries')
# print(dict_n.keys())  # Список только ключей
# print(dict_n.values()) # Список только значений
# print(dict_n.items()) # Список пар (список кортежей)
# 
# print('*' * 30)
# for key, value in dict_n.items():
#     print(f'{key}: {value}')
# # 
# print('first' in dict_n)
# print('third' not in dict_n)
# print('*' * 40)
# print(dict_n)
# for key in dict_n:
# # for key in dict_n.keys(): # то же самое
#     print(dict_n[key] * 2)

## Функция zip собирает кортежи
# a = ['red', 'orange', 'blue', 'green']
# b = [4545, 9889, 99, 121]
# print(list(zip(a, b)))
# new_dict = dict(zip(a, b))
# print(new_dict)

# ## Методы словаря
# print('Before: ', dict_n)
# # #Удаляем пару по ключу и возвращает значение
# del_item = dict_n.pop(2)
# print('After: ', dict_n)
# ## del_item = dict_n.pop() ## Error
# print('{} value of key 2'.format(del_item))

# # # # print('len = ', len(dict_n))

## Метод удаляет последнюю добавленную пару
# del_k_v_item = dict_n.popitem()
# print(dict_n)
# print(del_k_v_item)
# # # #
# # ## Пример со значениями
# if 13 not in dict_n.values():
#     dict_n['add'] = 13
# print(dict_n)

# words = {}  ## Пустой словарь - Falsy value
# words = {'string': 'value'}
# 
# ## Можем добавить другой словарь
# words.update({'more_values': 999, 'a': 7})
# print(words)
# 
# ## Вернет None, ошибки не будет
# print(words.get('c', 'Такого ключа нет'))
# 
# ## Создаем новую пару
# print(words.setdefault('b', 'значение по умолчанию'))
# print(words)

# ## V1
# result = dict()
# for char in 'thsathsathsuha':
#     if char not in result:
#         result[char] = 1
#     else:
#         result[char] += 1
# print(result)
# 
# ## V2
# result = dict()
# for char in 'thsathsathsuha':
#     result.setdefault(char, 0)
#     result[char] += 1
# print(result)
# 
# 
# # # 
# # # ## Удаление пары(ключ-значение) по ключу
# del words['b']
# print(words)

## Сложные словари. 
students =  {1122: ('Name', 'Surname', 'age', 'address'),
             1133: ('a_name', 'a_Surname','a_age', 'a_address')}
for key in students:
    if key == 1122:
        print(students[key][3])
# # #         
people =  {'Petrov': {'prof': 'student', 'age': 23},
            'Ivanov': {'prof': 'teacher','age': 43}}
print('Вложенные словари: ')
for key in people:
    print(people[key]['prof'])


### Синтаксис:
# lst = []      ## Список list
# tuples_a = () ## Кортеж tuple
# dict_a = {}   ## Словарь dictionary
# 
# ## Возвращает индекс элемента и значение
# for index, value in enumerate(students[1122]):
#     print(f'{index} -> {value}')
    

## Объединение словарей с версии 3.9
pprint(students | people)






