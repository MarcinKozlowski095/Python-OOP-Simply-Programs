"""
Zadanie 2: Klasa Rectangle
Napisz klasę Rectangle, która przechowuje długość i szerokość prostokąta.
Dodaj metody do obliczania i zwracania pola oraz obwodu prostokąta.
Dodatkowo dodaj metodę, która sprawdza, czy prostokąt jest kwadratem.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return  self.length * self.width

    def perimeter(self):
        return (2 * self.length) + (2 * self.width)

    def is_square(self):
        if self.length == self.width:
            return 'Is a square.'
        else:
            return 'Is a rectangle.'

shape1 = Rectangle(3,4)
shape2 = Rectangle(4,4)

print(shape1.area())
print(shape1.perimeter())
print(shape1.is_square())
print(shape2.is_square())
