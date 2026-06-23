# TODO: Aprender sobre keyword Arguments and Arguments


def add(*args):
    return sum(args)


add(3, 4, 5, 6)


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seats')


my_car = Car(make='Nissan', model='GT-R')
print(my_car.model)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
