'''
Задача № 1. Получить реверсную запись трехзначного числа
Пример: 
вход: 346, выход: 643
вход: 100, выход: 001
вход: 120, выход: 021
'''

number_to_reverse = int(input())

first_number = str(number_to_reverse // 100)
second_number = str(number_to_reverse // 10 % 10)
third_number = str(number_to_reverse % 10)

print(f'{third_number}{second_number}{first_number}')