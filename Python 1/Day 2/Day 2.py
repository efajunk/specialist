# start_deposit = int(input('Введите размер начального вклада: '))
# yearly_percent = int(input('Введите годовой процент начисления: '))
# total_years = int(input('Введите количество лет для вклада: '))
# 
# yearly_percent /= 100
# total = start_deposit * (1+yearly_percent)**total_years
# 
# print(f'Итоговая сумма на счету через {total_years} лет: {total:.2f} рублей')

# text_to_analyze = input()
# 
# preparing_to_lowing_case = text_to_analyze.lower()
# prepared_to_count = preparing_to_lowing_case.split()
# 
# print(prepared_to_count)
# articles = 0
# articles += prepared_to_count.count('a')
# articles += prepared_to_count.count('an')
# articles += prepared_to_count.count('the')

a, b, c, d = input('Введите четыре числа разделённые пробелом: ').split()
a, b, c, d = int(a), int(b), int(c) ,int(d)

count_of_zero = 0

if a, b, c, d == 0:
    count_of_zero += 1
# if b == 0:
#     count_of_zero += 1
# if c == 0:
#     count_of_zero += 1
# if d == 0:
    count_of_zero += 1
if count_of_zero == 0:
    print('Чисел равных нулю нет')
else:
    print(f'Количество числе равных нулю: {count_of_zero}')



















