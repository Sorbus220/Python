from sys import argv

name, salary, time, bonus = argv

try:
    result = int(salary) * float(time) + int(bonus)
    print(f"Ваша ЗП: {result}")
except ValueError:
    print("Введите число")
