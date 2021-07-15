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
import sys
def check_product(product_name):
    try:
        assert len(product_name) > 3
    except AssertionError:
        return 0,'Введите правильное наименование товара (количество символов больше 3)'
    else:
        return product_name

def check_quantity(quantity_product):
    try:
        assert float(quantity_product)
    except Exception:
        return 0,'Количество должно быть цифрой больше 0'
    else:
        return quantity_product

def check_phone(phone_number):
    try:
        assert phone_number.isdigit() and len(phone_number) == 10
    except AssertionError:
        return 0,'Контактный телефон должен содержать 10 цифр'
    else:
        return phone_number

def check_index(index):
    try:
        assert index.isdigit() and len(index) == 6 
    except AssertionError:
        return 0,'Индекс должен содержать 6 цифр'
    else:
        return index

def zakaz():
    product_name = input('Наименование товара (для выхода нажмите q): ')
    while not check_product(product_name)[0]:
        if product_name == 'q':
            break
        product_name = input(f'{check_product(product_name)[1]}\nНаименование товара (для выхода нажмите q): ')
    else:
        quantity_product = input('Количество товара (для выхода нажмите q): ')
        while not check_quantity(quantity_product)[0]:
            if quantity_product == 'q':
                break
            quantity_product = input(f'{check_quantity(quantity_product)[1]}\nКоличество товара (для выхода нажмите q): ')
        else:
            fio = input('Введите ФИО покупателя (для выхода нажмите q): ')
            while fio == 'q' or not fio:
                if fio == 'q':
                    break
                fio = input('Введите ФИО покупателя (для выхода нажмите q): ')
            else:
                phone_number = input('Введите телефон покупателя (для выхода нажмите q): ')
                while not check_phone(phone_number)[0]:
                    if phone_number == 'q':
                        break
                    phone_number = input(f'{check_phone(phone_number)[1]}\nВведите телефон покупателя (для выхода нажмите q): ')
                else:
                    index = input('Введите индекс покупателя (для выхода нажмите q): ')
                    while not check_index(index)[0]:
                        if index == 'q':
                            break
                        index = input(f'{check_index(index)[1]}\nВведите индекс покупателя (для выхода нажмите q): ')
                    else:
#                         with open('excellent_password.txt', 'w', encoding='utf-8') as password_export: password_export.write(password)
                        file_zakaz = open('C:\\Course\\Day_9\\zakaz_1.txt', 'w', encoding='utf-8')
                        print(product_name, file = file_zakaz)
                        print(quantity_product, file = file_zakaz)
                        print(fio, file = file_zakaz)
                        print(phone_number, file = file_zakaz)
                        print(index, file = file_zakaz)
                        file_zakaz.close()
                        print('Товарная накладная введена в файл C:\\Course\\Day_9\\zakaz_1.txt')
#                         return product_name, quantity_product, fio, phone_number, index

def in_out():
    """ In and Out function"""
    print('Ввод товарной накладной')            
    zakaz()


if __name__ == '__main__':
    in_out()       