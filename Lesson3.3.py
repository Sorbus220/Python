def my_func(var_1, var_2, var_3):
    if var_1 >= var_3 and var_2 >= var_3:
        return var_1 + var_2
    elif var_1 >= var_2 and var_1 >= var_3:
        return var_1 + var_3
    else:
        return var_2 + var_3


def my_func_use():
    try:
        print(
            f'Результат:{my_func(int(input("Введите 1ое число: ")), int(input("Введите 2ое число: ")), int(input("Введите 3ие число: ")))}')
    except ValueError:
        return print("Введите число!")


my_func_use()
