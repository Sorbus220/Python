russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_file = []
with open("text_4.txt", "r", encoding="utf-8") as file:
    for i in file:
        i = i.split(" ", 1)
        rus_file.append(russian[i[0]] + " " + i[1])
    print(rus_file)
with open("text_4_rus.txt", "w", encoding="utf-8") as file_ru:
    file_ru.writelines(rus_file)
