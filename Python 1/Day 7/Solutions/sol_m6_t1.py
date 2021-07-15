"""
Используя функцию random.randint(1, 1000) сформировать список
 из 20 элементов и сохранить в файл.
 После этого, считать числа из файла и найти максимальное и минимальное.
 """
## V1
import random as rnd

with open('test.txt', 'w') as write_file:
    random_digits = [rnd.randint(1, 1000) for i in (range(20))]
    print(*random_digits, file=write_file)
    
with open('test.txt') as read_file:
    list_of_digits = read_file.read().rstrip()    
    find_max = [int(i) for i in list_of_digits.split()]
    
print(f'{find_max =}')
print(max(find_max))
print(min(find_max))

