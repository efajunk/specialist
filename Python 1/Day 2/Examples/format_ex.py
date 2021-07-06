name = 'Student'
age = 10


'''Параметры sep(по умолчанию ' ') и end (по умолчанию '\n')'''
# print('hello', name, age, sep='|')
# print("Здравствуйте, ", name, ".", sep='', end=' ')
# print("Вам", age, "лет.")
# 
# ### 1-й способ - это %
# print('Result of our program <%s> and <%s>. Two values.' % (name, age))
# print('Result of our program %s. First value.' % name) # одна переменная
# print('Result of our program %s and %5i. Two values.' % (name, age))
# ## Вывод переменной с типом float
# ## с ограничением в 2 разряда после запятой
# print('Result of our program %.2f. First value.' % (age / 3))
# 
# ### 2-й способ - функция format
# print('Your name is {}. You are {}.'.format(name, age))
# print('You are {1}. Your name is {0}.'.format(name, age))
# print('You are {1}. Your name is {0}.'.format(name, age / 3))
# print('You are {1:.2f}. Your name is {0}.'.format(name, age / 3))
# print('You are {1:10.2f}. Your name is {0}.'.format(name, age / 3))
# 
### 3-й способ - f-string
print(f'Your name is {name} . You are {age}.')

# Можно подставлять и выражения
# print(f'Your name(three times) is {(name + " ") * 3}. You are {age / 3:.2f}.')
# 
b = 7
import math
# # 
print('34 строка:', 'Hello {}'.format('World')) 
print('35 строка:','{}'.format(math.pi))
print('36 строка:','{0:.4f}'.format(math.pi)) 
print('37 строка:','pos -> {0:+.2f}, neg -> {1:+.2f}'.format(5, -5))
print('38 строка:','{:.2e}'.format(3000))
print('39 строка:','{:0>6d}'.format(5456)) # Шесть позиций под вывод и заполнение нулями слева
print('40 строка:','{:x<7d}'.format(5))
print('41 строка:','{:,}'.format(1000000.99))
print('42 строка:','{:.1%}'.format(0.25)) # умножить на 100 и добавить знак %
print('43 строка:','{0}{1}'.format('a', 'b'))
print('44 строка:','{1}{0}'.format('a', 'b'))
print('45 строка:','{num:}'.format(num=3 * b))
print('46 строка:','{:^10d}'.format(333)) # Центрирование вывода






























