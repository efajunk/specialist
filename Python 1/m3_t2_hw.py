"""
Строка из 10 или менее слов.
Определите, сколько букв содержит самое длинное слово в строке.
Пример:
In: Как дела в учебе
Out: 5
"""

string = 'Как дела в учебе'
max_word_len = 0
letters_count = 0

for i in string:
    if i == ' ':
        letters_count = 0
        continue
    else:
        letters_count += 1
        if letters_count > max_word_len:
            max_word_len += 1
	
print(max_word_len)
