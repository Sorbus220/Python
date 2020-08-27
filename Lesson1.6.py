firstday = float(input("Введите результат пробежки первого дня: "))
overall = float(input("Введите какой результат Вы хотите достичь: "))
days = 1
km = firstday
while km < overall:
    firstday = firstday + firstday * 0.1
    days += 1
    km = firstday
print("Вы достигнете результать на %.d день" % days)
