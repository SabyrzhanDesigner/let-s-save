from random import randint

list = [randint(-10,10) for _ in range(20)]
print(list)
gen_list = (i ** 3 if i < 0 else i ** 2 for i in list if i % 2 == 0)
print(gen_list)
