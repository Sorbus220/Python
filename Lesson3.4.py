def my_func(a, b):
    return 1 / a ** abs(b)


print(my_func(2, -2))


def my_func_rec(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / (a * my_func_rec(a, -b - 1))
    else:
        return a * my_func_rec(a, b - 1)


print(my_func_rec(2, -2))
