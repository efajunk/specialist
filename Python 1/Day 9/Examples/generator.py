# a = (i ** 2 for i in range(3))
# 
# # print(a, type(a))
# print(next(a))
# print(next(a))
# print(next(a))
# # ## Чтобы не было ошибки StopIteration
# print(next(a, 'Элементы закончились'))
# 
# def gen():
#     a = 2
#     b = 2
#     yield a, b
#     
#     a += 2
#     yield a, b
#     
#     a *= 3
#     yield a, b
# 
# create = gen()
# print(type(create))
# print(next(create))
# print(next(create))
# print(next(create))
# print(next(create, 0))
# 
# def gen_for(n):
#     for item in range(n):
#         yield item ** 2
# #     
# #     
# res = gen_for(10)
# print(res, type(res))

def gen_string(text):
    ''' Generator '''
    for char in text:
        yield char.upper() + '!'
g = gen_string('hello')
for i in g:
    print(i)

print('*' * 40)
gen = (char.upper() + '!' for char in 'hello')
for i in gen:
    print(i)




