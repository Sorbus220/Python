from itertools import count, cycle
my_list = []

for el in count(int(input('Введите стартовое число '))):
    print(el)
    my_list.append(el+1)
    if el == 10:
        break

iterator = cycle(my_list)
print(my_list)
my_list = iter(my_list)
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))