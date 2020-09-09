my_list = [7, 5, 3, 3, 2]
rait = int(input("Введите число: "))
my_list.append(rait)
n = -1
for e in range(len(my_list) - 1):
    if my_list[n] > my_list[n - 1]:
        my_list[n], my_list[n - 1] = my_list[n - 1], my_list[n]
        n = n - 1
    else:
        break
print(my_list)
