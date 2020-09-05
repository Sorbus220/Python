def div(dividend, divider):
    try:
        res = dividend / divider
        print(res)
        return res
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        return


def div_use():
    try:
        div(int(input("Введите делимое: ")), int(input("Введите делитель: ")))
    except ValueError:
        print("Введите число")


div_use()
