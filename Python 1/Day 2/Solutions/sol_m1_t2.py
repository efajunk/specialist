'''
Задача №2
Найти каждую цифру трехзначного числа.
'''
## V1
chislo = int(input('Введите целое трёхзначное число (от 100 до 999) :'))
hundreds = chislo // 100
tenth = chislo % 100 // 10
ones = chislo % 10
print('Hundreds = ', hundreds, 'Tenth = ' , tenth, 'Ones = ', ones)

## V2
numbers = int(input('Введите целое трёхзначное число (от 100 до 999) :'))

first_place = numbers // 100
second_place = numbers // 10 % 10
last_place = numbers % 10

print('сотен', first_place)
print('десятков', second_place)
print('единиц', last_place)
