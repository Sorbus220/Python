class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def show_speed(self):
        return f'текущая скорость {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Превышение скорости!'
        else:
            return f'Скорость в пределах нормы'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Превышение скорости!'
        else:
            return f'Скорость в пределах нормы'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} на полицейском дежурстве'
        else:
            return f'{self.name} гражданский авто'


ferrari = SportCar(150, 'Красный', 'Ferrari', False)
kia = TownCar(50, 'Белый', 'Kia', False)
renault = WorkCar(70, 'Желтый', 'Renault', False)
ford = PoliceCar(120, 'Синий',  'Ford', True)

print(kia.show_speed())
print(f'Когда {kia.turn_right()}, {ferrari.go()}')
print(f'{ferrari.name} проезжает на красный свет')
print(f'{ford.police()} начинает преследование')
print(renault.show_speed())
