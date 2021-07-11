## Примеры множеств
ex = {3, 'hello', 3, 3, 2, 'a', 'a', 'b', 'a'}
print(ex, type(ex))

set_a = set([1, 2, 3, 4, 4, 2])
set_b = set([1, 5])
print(f'{set_a = }')
print(f'{set_b = }')

# ## Пересечение множеств
# ## Элементы, которые входят и в set_a и в set_b
print(set_a & set_b) 
# 
# ## Объединение множеств
# ## Элементы set_a или set_b
print(set_a | set_b)
# 
# ## Симметричная разность множеств
# ## Элементы set_a и set_b, кроме общих
print(set_a ^ set_b)
# 
# ## Разность множеств
# ## Элементы set_a, кроме тем, которые в set_b
print(set_a - set_b)


