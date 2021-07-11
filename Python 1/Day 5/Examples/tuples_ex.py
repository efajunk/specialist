## Кортежи - Неизменяемые списки(tuples)
a = 4, 1 ## Скобки не обязательно
print(a, type(a))
b = (3, 5, 'hello', True, 9)
c = tuple('hello')

p1, p2, p3, p4, p5 = b
print(p1, p2, p3, p4, p5)


## Распаковка
first, *medium, last = b
f, *_, prev_last, l = b

# ## Создание кортежа из одного элемента
one = 1, 
one_again = ('hello',)
print(f'{one = }')
print(f'{one_again = }')

print(b.count(9))
print(b.index(5))
# 
# ## Можно изменять элементы внутри списка
foo = ([4, 5], [44, 11, 90])
print(foo)
foo[0][0] = 99
print(foo)
foo[0].append(999)
print(foo)
# 
# 
lst = list(b)
print(f'{lst = }', type(lst))
new_tuple = tuple(lst)
print(f'{new_tuple = }', type(new_tuple))





