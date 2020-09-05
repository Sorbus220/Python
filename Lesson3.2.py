def data(name, surname, bdyear, city, email, phone):
    return print(
        f"Имя {name} Фамилия {surname} Город {city} Год рождения {bdyear} Email {email} Номер телефона {phone}")


data(name=input("Введите имя "), surname=input("Введите фамилию "), bdyear=input("Введите год рождения "),
     city=input("Введите город проживания "), email=input("Введите email "), phone=input("Введите номер телефона "))