import sys

def read_and_divide(filename):
    print()
    print("before " + filename)
    with open(filename, 'r') as fh:
      number = int(fh.readline())
      print('number: ', number)
      print('result:', 100 / number)
    print("after " + filename)
    print()

files = sys.argv[1:]

# for filename in files:
#     try:
#         read_and_divide(filename)
#     except Exception as err:
#         print(" There was a problem in " + filename)
#         print(" Text: {}".format(err))
#         print(" Name: {}".format(type(err).__name__))
# 
# ## IOError - отработка при доступе к несуществующему файлу
for filename in files:
    try:
        read_and_divide(filename)
    except (ZeroDivisionError, IOError):
        print("We have a problem with file {}".format(filename))




