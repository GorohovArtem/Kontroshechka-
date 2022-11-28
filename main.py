2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        print(f'C = {2 * pi * self.radius}')

    def area_of_circle(self):
        print(f'S = {pi * self.radius ** 2}')


circle = Circle(2.55)
circle.circumference()
circle.area_of_circle()
