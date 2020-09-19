def div():
    try:
        with open("text_5.txt", "w+", encoding="utf-8") as file:
            line = input("Введите числа через пробел: ")
            file.writelines(line + "\n")
            number = line.split()
            print(sum(map(int, number)))
    except IOError:
        print("Ошибка ввода-вывода!")
    except ValueError:
        print("Введите число!")


div()
