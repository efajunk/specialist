### Работает некорректно, есть несколько вопросов

"""
Сформировать данные для отправки заказа из
магазина по накладной и записать в файл:
1) Наименование товара.
2) Количество
3) ФИО покупателя
4) Контактный телефон (10 цифр)
5) Адрес(индекс(ровно 6 цифр), город, улица, дом, квартира)

Эти данные не могут быть пустыми.
Проверить правильность заполнения полей, используя исключения.
"""
import string as st
from pprint import pprint

ru_abc_l = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ru_abc_U = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def check_input(inp, key, count=0):
    try:
        if key == 'Наименование товара':
            symbols = ' ' + st.ascii_lowercase + st.ascii_uppercase + ru_abc_l + ru_abc_U
        if key == 'ФИО покупателя':
            symbols = ' ' + st.ascii_lowercase + st.ascii_uppercase + ru_abc_l + ru_abc_U    
        if key == 'Количество':
            symbols = '123456789'
        if key == 'Контактный телефон':
            symbols = st.digits    
        if key == 'Адрес':
            symbols = '1234567890'
        while count < 3:
            for char in inp:
                if char in symbols:
                    return True
                                        
            else:
                count +=1
                print(f'Ошибка ввода (введите данные в правильном формате)')
                key = key
                symbols = symbols
                inp = input(f'Повторно введите {key} :' )
                check_input(inp, key, count)
                
                
        
    except:
        print('Something went WRONG!!!')
        return False

def new_zakaz():
    zakaz = {'Наименование товара':'',
             'Количество': '', 
             'ФИО покупателя': '',
             'Контактный телефон': '',
             'Адрес': '' }

    for key in zakaz.keys():
        value = input(f'{key}:  ')
        if check_input(value, key):
            zakaz[key] = value
        else:
            return 'Поле заполнено неверно! Заказ не сформирован'

    for val in list(zakaz.values()):
        if val == '':
            print('Поле заполнено неверно! Заказ не сформирован')
            break
    else:
        print(f'Заказ сформирован \n {zakaz}')
        file_zakaz = open('C:\\Course\Day_9\\zakaz.txt', 'w', encoding='utf-8')
        print(zakaz, end='', file = file_zakaz)
        file_zakaz.close()
        
new_zakaz()