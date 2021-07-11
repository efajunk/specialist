"""
Дана строку. Необходимо посчитать количество вхождений
каждого символа.
Решения с помощью словаря
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
# string = input("Enter a string: ")
# dict_of_result = {}
# 
# for char in string:
#     if char not in dict_of_result:
#         dict_of_result[char] = string.count(char)
#     
# for char, count in dict_of_result.items():
#     print(f'{char}: {count}')
    
print('*' * 40)

## V2
# string = input("Enter a string: ")
# result = {}
# for char in string:
#     if char in result:
#         result[char] += 1
#     else:
#         result[char] = 1
#     
# for char, count in result.items():
#     print(f'{char}: {count}')
    

## V3
string = input("Enter a string: ")
result = {}
for char in string:
    ## Если ключ есть, то setdefault возвращает значение
    ## а если ключа нет, то setdefault создает ключ
    ## с указанным значением
    result.setdefault(char, 0)
    result[char] += 1
  
for char, count in result.items():
    print(f'{char}: {count}')
    
    
    
    
    
    
    
    
    
    
    
    
    
    