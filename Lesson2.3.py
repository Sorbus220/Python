seas_list = ["winter", "spring", "summer", "autumn"]
seas_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("Введите номер месяца: "))
if month == 1 or month == 12 or month == 2:
    print(seas_list[0])
    print(seas_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(seas_list[1])
    print(seas_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seas_list[2])
    print(seas_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seas_list[0])
    print(seas_dict.get(1))
elif month >= 13 or month == 0:
    print("Неверное значение месяца")
