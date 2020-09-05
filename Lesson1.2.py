seconds = int(input("Введите количество секунд: "))

hour = seconds // 3600

seconds %= 3600

minutes = seconds // 60

seconds %= 60
print("%02d:%02d:%02d" % (hour, minutes, seconds))
