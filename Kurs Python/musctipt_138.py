class Rectangle():
    """docstring for Rectangle"""

    def __init__(self, side_1=1, side_2=1):
        self.side_1 = side_1
        self.side_2 = side_2

    def rectangle_area(self):
        self.area = self.side_1 * self.side_2
        return self.area

    def __str__(self):
        message = "to jest prostokąt o bokach o bokach " + \
            str(self.side_1)+" oraz "+str(self.side_2)
        return message


class Square(Rectangle):
    def __init__(self, side_1=1):
        super().__init__(side_1, side_1)

    def square_area(self):
        return super().rectangle_area()

    def __str__(self):
        message = "to jest kwadrat o boku  "+str(self.side_1)
        return message


class Cube(Square):
    def __init__(self, side_1=1):
        super().__init__(side_1)

    def cube_area(self):
        return super().square_area() * 6

    def cube_volume(self):
        return super().square_area() * self.side_1

    def __str__(self):
        message = "to jest sześcian o boku  "+str(self.side_1)
        return message


rectangle = Rectangle(2, 5)
print(rectangle)
print("pole powierzchni wynosi", rectangle.rectangle_area())

square = Square(2)
print(square)
print("pole powierzchni wynosi", square.square_area())

cube = Cube(2)
print(cube)
print("pole powierzchni wynosi", cube.cube_area())
print("objętość wynosi", cube.cube_volume())
