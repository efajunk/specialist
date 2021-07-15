from pprint import pprint

def product_name(name_product):
    if name_product:
        return name_product
    return False

def product_count(count):
    if not count:
        count += 1
    return count

def fio(lst):
    try:
        dict_fio = {'Фамилия': '',
                    'Имя': ''}
        
        for index, key in enumerate(dict_fio.keys()):
            dict_fio[key] = lst[index]
        for value in dict_fio.values():
            value[0].upper()
        return dict_fio
    except:
        return False
    
def telefon_number(telefon):
    try:
        assert len(telefon) == 10 and telefon.isdigit()
    except Exception:
        return 'Ошибка ввода контактного номера телефона'
    return telefon

def address(address_customer):
    if (not address_customer or
        (len(address_customer[0]) != 6 and address_customer[0].isdigit())):
        return False
    return address_customer

def in_out():
    product = input('Введите наименование товара: ')
    if not product_name(product):
        product = input('Необходимо ввести наименование товара: ')
    else:        
        file_order = open('C:\\Course\\order.txt', 'w', encoding='utf-8')
        print(product, file=file_order)
        file_order.close()
    
    count = int(input('Введите количество товаров: '))
    file_order = open('C:\\Course\\order.txt', 'a', encoding='utf-8')
    print(count, file=file_order)
    file_order.close()
    
    lst = [i for i in input('Введите ФИО покупателя: ').split()]
    if (d_fio := fio(lst)):
        file_order = open('C:\\Course\\order.txt', 'a', encoding='utf-8')
        print(d_fio, file=file_order)
        file_order.close()
        
    telefon = input('Введите контактный номер телефона: ')
    if telefon_number(telefon) == 'Ошибка ввода контактного номера телефона':
        telefon = int(input('Номер телефона должен содержать 10 символов, введите снова: '))
    else:
        file_order = open('C:\\Course\\order.txt', 'a', encoding='utf-8')
        print(telefon, file=file_order)
        file_order.close()
        
    address_customer = [str(i) for i in input('Введите адрес покупателя:\n'
    'индекс(6 цифр), город, улица, дом, квартира: ').split()]
    if not address(address_customer):
        address_customer = [str(i) for i in input('Введите адрес покупателя строго по форме:\n'
        'индекс(6 цифр), город, улица, дом, квартира: ').split()]
    else:
        file_order = open('C:\\Course\\order.txt', 'a', encoding='utf-8')
        print(*address_customer, file=file_order)
        file_order.close()
        
if __name__ == '__main__':
    in_out()