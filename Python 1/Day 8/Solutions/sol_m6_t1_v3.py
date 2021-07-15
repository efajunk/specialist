def check_digits(password):
    counter_digits = 0
    for i in password :
        if i.isdigit():
            counter_digits += 1
            if counter_digits >= 1:
                return True
    return False


def special_symbol(password):
    special = '_!@#$%^&'
    for i in password:
        if i in special:
            return True
    return False


def string_upper(password):
    for i in password:
        if i.isupper():
            return True
    return False
            

def string_lower(password):
    for i in password:
        if i.islower():
            return True
    return False    
    
def save_password(password): 
    if ((7 < len(password) < 16) and
        check_digits(password) and
        special_symbol(password) and
        string_lower(password) and
        string_upper(password)):
        file_out = open('C:\\Course\\Day_8\\passwords.txt', 'w')
        print(password, file=file_out)
        file_out.close()
        return "Success"
    return "Epic fail"
    
password = input('Enter password: ')
count = 4
while save_password(password) == "Epic fail" and count > 0:
    print("Epic fail")
    password = input('Enter password: ')
    count -= 1
