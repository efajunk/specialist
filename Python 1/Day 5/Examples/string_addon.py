import string
# 
# data = input('Enter a string: ')
# 
# ## Разделение по любой строке
# # result = data.split('aaa', 2)
# # print(*result)
# 
# 
# # ## Удаляем пробельные символы в начале и в конце строки
# print('start:', data.strip(), 'finish')
# # 
# # ## Удаляем пробельные символы только в начале строки
# print('start:', data.lstrip(), 'finish')
# # 
# # ## Удаляем пробельные символы только в конце строки
# print('start:', data.rstrip(), 'finish')
# # 
# # ## Замена одной подстроки на другую
# string = 'sah  asotuhas  a'
# new_string = string.replace('  ', ' ')  ## Out -> 'sah asotuhas a'
# print(new_string)

## Полезные константы
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)