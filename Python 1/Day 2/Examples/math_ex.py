# 
a = 5
b = 2
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)    # Тип результа всегда float!
print('a // b =', a // b)  # Целочисленное деление -> out: 2
print('a % b =', a % b)   # Остаток от деления -> out: 1
print('a ** b =', a ** b) # Возведение в степень -> out: 25
print('(a ** b) ** 0.5 =', (a ** b) ** 0.5) # Извлечение квадрата


# ### Синтаксический сахар
# print(f'{a = }') ## Только с версии 3.9

a = a + 1  # a += 1
print('a =', a)
# 
a += 1  # a = a + 1
print('a +=', a)
# 
a -= 2  # a = a - 2
print('a -=', a)
# 
a *= 3  # a = a * 3
print('a *=', a)
# 
b /= 4 # b = b / 4
print('b /= %.2f' % b)

a //= 3
print('a //= ', a)

a %= 2
print('a %= ', a)
# a += 2
# 
# # Длинная арифметика
# a **= 300
# print(a)
# # # 
print(float('inf'))  ## Плюс бесконечность. Самое большое число
print(float('-inf')) ## Минус бесконечность. Самое маленькое число
# 
# ## Важный момент хранение дробных чисел в памяти компьютера
# a = 0.1 * 3
# print(a == 0.3)







