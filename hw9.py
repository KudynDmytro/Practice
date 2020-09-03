from math import sqrt
# Создайте класс "Triangle", который инициируется с помощью трех точек.
# Реализуйте в классе метод вычисления площади треугольника.
# * Для "Triangle", на основании его точек, реализуйте возможность узнать к какому типу он относится:
# правильный (три стороны равны),
# равнобедренный (две стороны равны), "египетский"


class Point:
    _x = None
    _y = None

    def __init__(self, x, y):
        # check type here
        self._x = x
        self._y = y

    def __add__(self, other):
        if type(self) == type(other):
            return Line(self, other)

    def __sub__(self, other):
        if type(self) == type(other):
            return Line(self, other)


class Line:
    _point1 = None
    _point2 = None

    def __init__(self, a, b):
        # check type Point a, b here
        self._point1 = a
        self._point2 = b

    def length(self):
        k1 = self._point1._x - self._point2._x
        k2 = self._point1._y - self._point2._y

        return sqrt(k1**2 + k2**2)


#points of triangle
p1 = Point(1, 4)
p2 = Point(1, 1)
p3 = Point(4, -3)


class Triangle:
    def __init__(self, a1, a2, a3):
        if type(a1) == type(a2) == type(a3):
            self._a1 = a1
            self._a2 = a2
            self._a3 = a3

    def square(self):
        self.l1 = Line.length(self._a1 + self._a2)
        self.l2 = Line.length(self._a2 + self._a3)
        self.l3 = Line.length(self._a1 + self._a3)
        self.p = (self.l1 + self.l2 + self.l3) / 2
        if self.l1 == self.l2 == self.l3:
            print('это правильный треугольник')
        elif self.l1 == self.l2 or self.l1 == self.l3:
            print('это равнобедренный треугольник')
        elif self.l1 / self.l2 / self.l3 == 3 / 4 / 5:
            print('это египетский треугольник')
        return sqrt(self.p * (self.p - self.l1) * (self.p - self.l2) * (self.p - self.l3))


tria = Triangle(p1, p2, p3)
sq = tria.square()
print(sq)

# Создайте класс "Circle", который работает как окружность.
# Реализуйте в классе метод вычисления площади фигуры.


class Circle:
    PI = 3.1415

    def __init__(self, o, r):
        self._o = o
        self._r = r
        self.radius = Line.length(self._o + self._r)

    def square(self):
        return self.PI * self.radius ** 2


p4 = Point(0, 0)
p5 = Point(4, 3)
c = Circle(p4, p5)
print(c.square())
