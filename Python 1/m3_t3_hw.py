"""
Дана строка из символов(латинские буквы + цифры)
Нужно вывести новой строкой только цифры, если они есть или
написать, что их нет.
Пример: 
In: 'antuh1ouou21au3'
Out: 1213
"""

string_input = input()
string_of_digit = ''

for i in string_input:
	if i.isdigit():
		string_of_digit = string_of_digit + i

if len(string_of_digit) == 0:
	print(f'В введенной строке ({string_input}) нету чисел')
else:
	print(f'Цифры из введённой строки: {string_of_digit}')
		
