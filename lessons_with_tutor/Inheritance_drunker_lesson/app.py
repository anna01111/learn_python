import math


class Drunkard:

    def __init__(self, name, do):
        self.name = name
        self.do = do # drinking norm
        self.d = 0
        self.lo = 1  # meter
        self.l = self.lo

    def __repr__(self):
        return f"""
        My name is {self.name}
        My drinking norm is {self.do}
        Length of my step is {self.lo}
        I have drunk {self.d} ml of alcohol
        Now length of my step is {self.l}
        """

    def drink(self, quantity):
        self.d += quantity

    def step(self):
        upper_part = (self.d - self.do) ** 2
        down_part = 10 * (self.do ** 2)
        both_parts = - (upper_part / down_part)
        self.l = self.lo * math.exp(both_parts)
        return self.l


# lst = [Drunkard('Anatoliy', 1500)]
#
# tolik.drink(500)
# tolik.step()
# print(tolik)

lst = []
while True:
    try:
        number_of_drunkards = int(input('Enter number of drunkards: '))
        break
    except ValueError:
        print('Incorrect number, try again')

for i in range(number_of_drunkards):
    name = input("Please enter name: ")
    drinking_norm = int(input(f"Please enter drinking_norm for {name}: "))
    lst.append(Drunkard(name, drinking_norm))

party = True
while party:
    print('We entered a bar')
    quantity_of_alcohol = int(input('How Much do we drink here? '))
    for el in lst:
        el.drink(quantity_of_alcohol)
        res = el.step()
        print(el)
        if res < 0.1:
            print(f'{el.name} has finished and went to bed')
            party = False
            break

print('End of drinking...')
