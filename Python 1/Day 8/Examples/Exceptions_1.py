import sys
## Работа с исключениями

## Пример 1
# try:
#     ## Блок инструкций
#     print('Before')
#     1 / 0  ## Выполнение try прекращается и начинает работать блок except
#     print('After')
# except:
#     print("You cannot divide by zero!")
# # # # 
# print('Done')

## Пример 2
# my_dict = {"a":1, "b":2, "c":3}
# try:
#     value = my_dict["d"]
#     print("You'll never see its message")
# except KeyError:
#     print("That key does not exist!")
#     
# ## Пример 3
# my_list = [1, 2, 3, 4, 5]
# my_dict = {"a":1, "b":2, "c":3}
# try:
#     my_list[6]
#     my_dict[1]
# except (IndexError, KeyError):
#     print('Oops, there is an error')
#     
## Пример 4
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
    lst = list(range(4))
    print(lst[3])
    a = 1 / 0
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except Exception as err:
    print("Some other error occurred!", err)
    
## Пример 5 
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["a"]
    1/0
except KeyError:
    print("A KeyError occurred!")
    
## Блок else отработает только в случае отсутствия исключения
else:
    print("No error occurred!")
    sys.exit()

## Блок finally отработает в любом случае
finally:
    print("The finally всегда отработает!")
# 
# assert проверяет истинность какого-либо выражения
# ###  код работает дальше
# a = 5
# b = 7
# assert True
# assert a < b, 'Error occured when a > b'  
# # 
# try:
#     assert a > b
# 
# except AssertionError:
#     print('Условия не выполнилось')
# # 
# print('All have checked')
#  
#     
# ## Пример 6 
# a = 0
# b = 7
# if not a:
#     raise ZeroDivisionError('Нехорошо вводить нуль при делении')
# else:
#     raise Exception
    






