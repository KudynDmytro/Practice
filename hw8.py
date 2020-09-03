import hw7
# Напишите декоратор, который замеряет время выполнения задекорированой функции.
# Замеряйте время выполнения функций из предидущего дз.


def decorator_1(func):
    def wrap():
        s = input('Enter start time:')
        res = func()
        z = input('Enter end time:')
        if ':' in s and z:
            print('The function had been building for', int(z.split(':')[0]) - int(s.split(':')[0]), 'hours and',
                  int(z.split(':')[1]) - int(s.split(':')[1]), 'minutes')
        return res
    return wrap()


@decorator_1
def fun1():
    hw7.classes()

# "Навигация". Создайте класс Point() который отвечает за точку на карте.
# У обьектов класса должны быть две координаты - широта\долгота (обязательные, неизменяемые),
# название и ссылка на описание (не обязательные, изменяемые).
# Обеспечьте проверку данных для всех параметров.


class Point:
    def __init__(self, latitude, longitude, name = None):
        if type(latitude) == int or float:
            self._latitude = latitude
        else:
            print('coordinates can be only ', float, 'or ', int)
        if type(longitude) == int or float:
            self._longitude = longitude
        else:
            print('coordinates can be only ', float, 'or ', int)
        if name == None:
            self.info = f"This dot's coordinates are:\n{latitude} - latitude\n{longitude} - longitude"
        else:
            self.info = f"This dot's coordinates are:\n{latitude} - latitude\n{longitude} - longitude. " \
                        f"\nDot's name is {name}"


s = Point(234, 23.3)
a = Point(2, 12, 'Zipper')
print(s.info)

# создайте декоратор, который бы проверял время запуска функции,
# и если функция запущена период с 06-00 до 10-00 выводил "Доброе утро" и выполнял функцию,
# с 10-00 до 18-00 - "Добрый день",
# с 18-00 до 08-00 - "Надо спать" и не выполнял функцию


def decorator_2(func):
    def wrap():
        r = input('Enter start time:')
        e = r.split(':')
        if int(e[0]) in range(6, 10):
            if int(e[1]) in range(0, 60):
                print('GOOD MORNING')
                res = func()
                return res
        elif int(e[0]) == 10 and int(e[1]) == 0:
            print('GOOD MORNING')
            res = func()
            return res
        elif int(e[0]) in range(10, 19):
            if int(e[1]) in range(0, 60):
                print('GOOD AFTERNOON')
                res = func()
                return res
        elif int(e[0]) == 18 and int(e[1]) == 0:
            print('GOOD AFTERNOON')
            res = func()
            return res
        elif int(e[0]) in range(18, 23):
            if int(e[1]) in range(0, 60):
                print('YOU NEED TO SLEEP')
                return
        elif int(e[0]) in range(0, 6):
            if int(e[1]) in range(0, 59):
                print('YOU NEED TO SLEEP')
                return
    return wrap()


@decorator_2
def fun2():
    hw7.classes()
