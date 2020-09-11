with open("text_1.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f'Содержимое файла: \n {content}')
    file.seek(0)
    content = file.readlines()
    print(f'Количество строк в файле - {len(content)}')
    file.seek(0)
    content = file.readlines()
    for i in range(len(content)):
        print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
    file.seek(0)
    content = file.read()
    content = content.split()
    print(f'Общее количество слов - {len(content)}')