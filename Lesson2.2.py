elements = int(input("Введите количество элементов в списке: "))
my_list = []
i = 0
el = 0
while i < elements:
    my_list.append(input("Введите значение списка: "))
    i += 1
for e in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)
