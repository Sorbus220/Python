class Road:
    def __init__(self, _length, _width, weight, height):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.height = height

    def total(self):
        count = self._length * self._width * self.height * self.weight
        return count


r = Road(20, 5000, 25, 5)
print(f'Необходимо {r.total() / 1000} т')
