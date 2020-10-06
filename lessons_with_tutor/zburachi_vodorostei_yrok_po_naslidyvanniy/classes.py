import math


class Collector:

    def __init__(self, name, speed, fatigue_factor):
        self.name = name
        self.speed = speed
        self.fatigue_factor = fatigue_factor
        self.money = 0

    def __repr__(self):
        return f'{self.name} ({self.__class__.__name__}) with speed {self.speed:.2f} and factor of fatigue {self.fatigue_factor}'

    def work(self):
        quantity = self.speed
        self.speed = self.speed * (1 - self.fatigue_factor)
        return quantity

    def pay(self, salary):
        pass


class Dolphin(Collector):

    def __init__(self, name):
        Collector.__init__(self, name, 15, 0.1)


class Diver(Collector):

    def __init__(self, name):
        Collector.__init__(self, name, 0, 0.3)
        self.coef = 0.3  # коэффициент пропорциональности–0.3кг/грн
        self.salary = 0

    def __repr__(self):
        return f'{self.name} ({self.__class__.__name__}) with salary {self.salary}, speed {self.speed:.2f} and factor of fatigue {self.fatigue_factor}'

    def pay(self, salary):
        self.salary = salary
        if 0 < self.salary <= 120:
            self.speed = self.salary * self.coef
        if self.salary > 120:
            self.speed = 120 * self.coef


class Volunteer(Collector):
    def __init__(self, name):
        Collector.__init__(self, name, 0, 0.4)
        self.salary = 0

    def __repr__(self):
        return f'{self.name} ({self.__class__.__name__}) with salary {self.salary}, speed {self.speed:.2f} and factor of fatigue {self.fatigue_factor}'

    def pay(self, salary):
        self.salary = salary
        self.speed = 10 * (1 - math.exp(-0.2 * self.salary))


class Cyborg(Collector):
    def __init__(self, name='IC1000'):
        Collector.__init__(self, name, 7, 0.01)
        self.time_worked = 0

    def work(self):
        quantity = self.speed
        self.time_worked += 1
        if self.time_worked < 4:
            self.speed = self.speed * (1 - self.fatigue_factor)
        else:
            self.speed = 0
        return quantity  # кількість водоростей зібраних за годину


