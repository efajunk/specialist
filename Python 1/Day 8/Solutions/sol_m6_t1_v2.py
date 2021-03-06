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
import os

def drop_check() -> list:
    recheck = [0, 0, 0, 0]
    return recheck

def unpack_mistakes_keys(dict_of_mistakes):
    mistakes_names_out = []
    for i in dict_of_mistakes.keys():
        mistakes_names_out.append(i)
    return mistakes_names_out

def mistakes_initiate() -> dict:
    mistakes_dict = {
    'upper' : 'Не хватает буквы в верхнем регистре',
    'lower' : 'Не хватает буквы в нижнем регистре',
    'digits' : 'Не хватает цифры',
    'specials' : 'Не хватает спецсимвола'
    }
    return mistakes_dict

def password_check(pass_check, dict_of_mistakes=mistakes_initiate()):
    mistakes_names = unpack_mistakes_keys(mistakes_initiate())
    check = drop_check()
    mistakes = dict_of_mistakes
    uppercase = st.ascii_uppercase
    lowercase = st.ascii_lowercase
    digits = st.digits
    specials = '_!@#$%^&'
    if 16 > len(pass_check) > 8:
        for i in pass_check:
            if i in uppercase:
                check[0] = 1
                mistakes[mistakes_names[0]] = 0
                break
        for i in pass_check:        
            if i in lowercase:
                check[1] = 1
                mistakes[mistakes_names[1]] = 0
                break
        for i in pass_check:            
            if i in digits:
                check[2] = 1
                mistakes[mistakes_names[2]] = 0
                break
        for i in pass_check:            
            if i in specials:
                check[3] = 1
                mistakes[mistakes_names[3]] = 0
                break
    else:
        return 'len_error', mistakes
    if min(check) == 1:
        return True, mistakes
    return False, mistakes

def count_check(count_in: int) -> str:
    if count_in != 0:
        return f'Осталось попыток {count_in}'
    else:
        return f'Попыток больше не осталось. Попробуйте позже.'


def greet():
    print('*'* 80)
    print('Здравствуй человек! Тебе предстоит ввести правильный пароль, состоящий из:\n'
        '1. Цифр\n'
        '2. Букв латинского алфавита(строчные и прописные)\n'
        '3. Специальных символов special = "_!\@#$%^&".\n'
        'Всего 4 набора различных символов.\n'
        'В пароле обязательно должен быть хотя бы один символ из каждого набора.\n'
        'Длина пароля от 8(мин) до 15(макс) символов.\n'
        'Максимальное количество попыток ввода неправильного пароля - 5.')
    print('*'* 80)
    
def password_start(password):
    check = drop_check()
    uppercase = st.ascii_uppercase
    lowercase = st.ascii_lowercase
    digits = st.digits
    specials = '_!@#$%^&'
    mistakes_out = mistakes_initiate()
    flag = True
    for count in range(4, -1, -1):
        if password and flag:
            flag = False
        else:
            greet()
            password = input('Введите пароль: ')
        checking_result, mistakes_out = password_check(password, mistakes_initiate())
        if checking_result == True:
            print(f'Вы великолепны! Пароль будет записан в {os.path.abspath(os.getcwd())}\excellent_password.txt')
            with open('excellent_password.txt', 'w', encoding='utf-8') as password_export:
                password_export.write(password)
            break
        elif checking_result == 'len_error':
            print('Недостаточная длинна пароля или введённый пароль слишком длинный.\n'
            f'Требуемая длинна 8 до 15. Длинна введённого пароля: {len(password)}')
            print(count_check(count))
            check = drop_check()
            continue
        
        else:
            print(f'Пароль не отвечает необходимым требованиям. Попробуйте ещё раз.')
            mistakes_names = unpack_mistakes_keys(mistakes_initiate())
            if mistakes_out[mistakes_names[0]]:
                print(mistakes_out[mistakes_names[0]])
            if mistakes_out[mistakes_names[1]]:
                print(mistakes_out[mistakes_names[1]])
            if mistakes_out[mistakes_names[2]]:
                print(mistakes_out[mistakes_names[2]])
            if mistakes_out[mistakes_names[3]]:
                print(mistakes_out[mistakes_names[3]])
            check = drop_check()
            print(count_check(count))
            


def in_out():
    """ In and Out function"""
    greet()        
    password = input('Введите пароль: ')            
    password_start(password)


if __name__ == '__main__':
    in_out()

