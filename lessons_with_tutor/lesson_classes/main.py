from classes import Person, Car

person1 = Person('Ania', 'Lozynska', 28, '0630000000')
person1.info()
person1.name = 1
# person1.__age = 22
# person1.info()
person1.set_age(22)
person1.info()
person1.age = 45
person1.info()

person1.phone_num = '00000'
print(person1.phone_num)


ca1 = Car('Audi')
ca1.info()
ca1.move(85)
print(ca1)
person1.have.append(ca1)

ca2 = Car('Jaguar')
person1.have.append(ca2)

lst = [Person('Olia', 'Loz', 20, '0400000'), Person('Yura', 'Zra', 26, '0770000')]
for el in lst:
    print(el)


lst.append(person1)
print()

for el in lst:
    print(el)