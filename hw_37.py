# list = [i for i in range(1, 8)]
# print(list)
#
# gen = {i:i**3 for i in list if i % 2 != 0}
# print(gen)

# list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# print(list)
#
# gen = {i for i in list if i % 2 == 0}
# print(gen)

# gen = [i for i in range(0, 100, 10)]
# print(gen)

# def gen_func():
#     yield 1
#     yield 2
#
# def ord_func():
#     return (i for i in range(1,2))
#     return (i for i in range(2,3))
#
# gen_func = gen_func()
# print(next(gen_func))
# print(next(gen_func))
#
# print('divider')
#
# ord_func = ord_func()
# print(next(ord_func))
# print(next(ord_func))

def gen_func(n):
    for i in range(0, n):
        if i % 7 == 0:
            yield i

gen_func = gen_func(67)
print(*gen_func)
