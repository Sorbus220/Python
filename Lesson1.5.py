revenue = float(input("Введите значение прибыли: "))
charge = float(input("Введите значение издержки: "))
if revenue > charge:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {revenue / charge:.2f}")
    employes = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль фирмы в расчете на одного сотрудника {(revenue - charge) / employes:.2f}")
elif revenue == charge:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
