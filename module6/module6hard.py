import math


class Figure:

    sides_count = 0

    def __init__(self, sides, color, filled=False):
        self.__sides = list(map(int, sides))
        self.__color = list(color)
        self.filled = bool(filled)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        return all(0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.color = (r, g, b)
            return self.color
        raise ValueError("Введен некорректный цвет")

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != len(self.__sides):
            raise ValueError('Количество сторон не совпадает')

        res = all(
            isinstance(side, (int, float)) and side > 0 for side in new_sides)
        print('res:', res)
        if not res:
            raise TypeError('Введены неправильные значения сторон')

        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            raise ValueError("Количество сторон не совпадает")

        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, length, color, filled=False):
        super().__init__(length, color, filled)
        self.__radius = length / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius**2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = (self.__sides[0] + self.__sides[1] + self.__sides[2]) / 2
        square = math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) *
                           (p - self.__sides[2]))
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, length, color, filled=False):
        sides = [length] * self.sides_count
        super().__init__(sides, color, filled)

    def get_volume(self):
        return self.__sides[0]**3


