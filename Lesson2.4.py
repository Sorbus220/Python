text = input("Введите текст: ")
words = []
num = 1
for e in range(text.count(' ') + 1):
    words = text.split()
    if len(words[e]) <= 10:
        print(f" {num} {words[e][0:10]}")
        num += 1
    else:
        print(f" {num} {words[e] [0:10]}")
        num += 1
