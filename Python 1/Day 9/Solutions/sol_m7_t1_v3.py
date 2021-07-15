def check_number(number_to_check):
    if number_to_check.startswith('8') or number_to_check.startswith('7'):
        number_to_check = number_to_check[1:]
    elif number_to_check.startswith('+7'):
        number_to_check = number_to_check[2:]
    if (number_to_check.startswith('9') and
        len(number_to_check) == 10 and
        number_to_check.isdigit()):
        return number_to_check
    else:
        raise Exception

def save_order(order_to_save=None):
    if order_to_save is None:
        return 'Bad order'
    else:
        with open('order.txt', 'w', encoding='utf-8') as order_file:
            for key, value in order_to_save.items():
                temp = key + ': ' + str(value) + '\n'
                order_file.write(temp)
        return 'Good order have recorded in "order.txt"'

def quest_initiate() -> dict:
    card_of_order = {}
    product_name = input('Введите наименование товара: ')
    if product_name:
        card_of_order['Наименование товара'] = product_name
        
    amount = float(input('Введите количество товара: '))
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
    if len(card_of_order) == 5:
        return card_of_order
    return None

if __name__ == '__main__':
    print(save_order(quest_initiate()))