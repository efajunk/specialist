def check_number(number_to_check):
    if number_to_check.startswith('8') or number_to_check.startswith('7'):
        number_to_check = number_to_check[1:]
    elif number_to_check.startswith('+7'):
        number_to_check = number_to_check[2:]
    if number_to_check.startswith('9') and len(number_to_check) == 10:
        return number_to_check
    else:
        raise Exception

def save_order(order_to_save):
    with open('order.txt', 'w') as order_file:
        for i, j in order_to_save.items():
            temp = i + ': ' + j + '\n'
            order_file.write(temp)

def quest_initiate() -> dict:
    card_of_order = {}
    product_name = input('Введите наименование товара: ')
    if product_name:
        card_of_order['Наименование товара'] = product_name
        
    amount =(input('Введите количество товара: '))
    if amount:
        card_of_order['Количество товара'] = amount
        
    full_name = input('Введите ваши имя и фамилию: ')
    if full_name:
        card_of_order['ФИО покупателя'] = full_name

    while True:
        phone_number = input('Введите ваш номер телефона: 8')
        try:
            card_of_order['Контактный телефон'] = check_number(phone_number)
            break
        except:
            print('Номер введён неверно, попробуйте ещё раз')

    address = input('Введите ваш адрес: ')
    if address:
        card_of_order['Адрес'] = address
    return card_of_order

if __name__ == __main__:
    save_order(quest_initiate())

