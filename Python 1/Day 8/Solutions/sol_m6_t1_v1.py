'''
Задача №1
Вход:
Пользователь должен ввести правильный пароль, состоящий из:
цифр, букв латинского алфавита(строчные и прописные) и специальных символов  special = '_!@#$%^&'.
Всего 4 набора различных символов.
В пароле обязательно должен быть хотя бы один символ из каждого набора.
Длина пароля от 8(мин) до 15(макс) символов.
Максимальное количество попыток ввода неправильного пароля - 5.
Каждый раз выводим номер попытки.
Желательно выводить пояснение, почему пароль не принят и что нужно исправить.

import string as st
st.digits
st.ascii_lowercase
st.ascii_uppercase
special = '_!@#$%^&'

Выход:
Написать, что ввели правильный пароль и записать его в файл pass.txt

Пример: 
хороший пароль -> o58anuahaunH!
хороший пароль -> aaaAAA111!!!
плохой пароль -> saucacAusacu8
'''
import string as st
    
def password():
    """Check password"""
    specials = '_!@#$%^&'
    print('''Придумайте пароль состоящий из цифр, букв латинского алфавита(строчные и прописные)
         и специальных символов. Длина пароля от 8(мин) до 15(макс) символов.
         На придумывание правильного пароля у вас есть 5 попыток''')
    count = 0
    
    while count < 5:
        errors = sp = d = lw = up = dl = ''
        pss = input(f'Попытка №{count+1} \n Введите пароль :')
   
        for char in pss:
            if char in specials:
               sp = "ok"
               break
        else:
            errors += 'В пароле отсутствуют спецсимволы.\n'

        for char in pss:
            if char in st.digits:
               d = "ok"
               break
        else:
           errors += 'В пароле отсутствуют цифры.\n'

        for char in pss:
            if char in st.ascii_lowercase:
               lw = "ok"
               break
        else:
           errors += 'В пароле отсутствуют символы нижнего регистра.\n'

        for char in pss:
            if char in st.ascii_uppercase:
               up = "ok"
               break
        else:
            errors += 'В пароле отсутствуют символы верхнего регистра.\n'
        
        if len(pss) < 8 or len(pss) > 15:
              errors += 'Длина пароля не соответствует значению от 8 до 15.\n'
        else:
              dl = "ok"
        if sp == d == lw == up == dl == "ok":
            print('Пароль хороший. Файл с паролем сохранён в E:\password.txt')
            file_pss = open('C:\\Course\\password.txt', 'w', encoding='utf-8')
            print(pss, end='', file = file_pss)
            file_pss.close()
            break
        else:
            print(errors)
        count +=1
        
        
password()