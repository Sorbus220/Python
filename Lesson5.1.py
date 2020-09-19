with open("text_1.txt", "w", encoding="utf-8") as file:
    line = input('Введите текст ')
    while line:
        file.write(line + "\n")
        line = input('Введите текст ')
        if line == "Q":
            break
