class Person:

    def __init__(self, name, surname, age, phone_num):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__phone_num = phone_num
        self.have = []

    def __str__(self):
        s = ''
        for el in self.have:
            s += f'{el}'
        return f'My name is {self.__name}, my surname is {self.__surname}, my age is {self.__age}, my phone number is {self.__phone_num}, I have {s}'

    def info(self):
        print('My name is', self.__name, 'my surname is', self.__surname, 'my age is ', self.__age, 'my phone number is', self.__phone_num)

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print('Incorrect age')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def phone_num(self):
        return self.__phone_num

    @phone_num.setter
    def phone_num(self, phone_num):

        # is_num = True
        # for el in phone_num:
        #     if '0' <= el <= '9':
        #         continue
        #     else:
        #         is_num = False
        #         break
        # if is_num:
        #     self.__phone_num = phone_num
        # else:
        #     print("Incorrect phone number")

        for el in phone_num:
            if el not in '0123456789()+ ':
                print('Incorrect phone number')
                break

        # following line is executed when the loop terminates through exhaustion of the iterable
        # following line is NOT executed when the loop is terminated by a break statement
        else:
            self.__phone_num = phone_num


class Car:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Car {self.name}'

    def info(self):
        print('I am a car - ', self.name)

    def move(self, speed):
        print(self.name, "moves with speed", speed, "km/h")
