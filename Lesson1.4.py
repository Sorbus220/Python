n = int(input("Введите целое положительное число: "))
maximum = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > maximum:
        maximum = n % 10
    if n > 9:
        continue
    else:
        print("Максимальная цифра в числе: ", maximum)
        break
