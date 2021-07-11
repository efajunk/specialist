"""
Дана последовательность из N чисел. Найти в ней два самых маленьких числа.
Последовательность можно сформировать с помощью функции randint()
Вариант 1.
from random import randint
nums = []
for _ in range(20):
    nums.append(randint(1, 100)) ## Границы интервала от 1 до 100
    
Вариант 2.
from random import randint
res = [randint(1, 100) for _ in range(20)]
"""
## V1
# from random import randint
# num_seq = []
# for _ in range(20):
#     num_seq.append(randint(1,100))
#     
# result_num_seq = num_seq.copy()
# result_num_seq.sort()
# print(f'В заданной последовательности: \n{num_seq} \n'
#       f'два самых маленьких числа: {result_num_seq[0]} и '
#       f'{result_num_seq[1]}.')

## V2
# from random import randint
# 
# N = 20
# res = [randint(1, 100) for _ in range(N)]
# res.sort()
# print(res)
# if res[1] == res[0]:
#     print(res[0],res[2])
# else:
#     print(res[0], res[1])


## V3
# from random import randint
# nums = []
# for _ in range(20):
#     nums.append(randint(1, 100))
# print(*nums)
# 
# min_value_1 = nums[0]
# for n in nums[1:]:
#     if n < min_value_1:
#         min_value_1 = n
# 
# nums.remove(min_value_1)
# 
# min_value_2 = nums[0]
# for n in nums[1:]:
#     if n < min_value_2:
#         min_value_2 = n
# 
# print(f'{min_value_1 = }')
# print(f'{min_value_2 = }')


## V4
from random import randint
res = [randint(1, 100) for _ in range(20)]
print(res)

for j in range(2):
    item_min = 101
    for i in range(len(res)):
        if res[i] < item_min:
            item_min = res[i]
       
    print(f'Самое самое маленькое число в списке: {item_min}')
    min_index = res.index(item_min)
    res.pop(min_index)


## V5 Поиск 2 уникальных минимальных элементов
from random import randint
res = [randint(1, 100) for i in range(20)]
small_one = the_smallest = 101
print(res)

for i in res:
    if i < small_one:
        small_one = i
## Удаляем все повторы 1-го минимального числа       
while small_one in res:        
    res.remove(small_one)

for i in res:
    if i < the_smallest:
        the_smallest = i

print(small_one, the_smallest)
































