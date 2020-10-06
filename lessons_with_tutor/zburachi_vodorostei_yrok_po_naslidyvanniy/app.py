import random
from classes import Dolphin, Diver, Volunteer, Cyborg

from collections import OrderedDict

workers = []
salary = 0


def menu():

    global workers

    # набір бригади
    action = 'y'
    while action == 'y':
        action = input('Do you want to create a worker? y/n')
        if action != 'y':
            print('The End')
            break
        a_type = input('Please enter a type: d for Dolphin, i for Diver, v for Volunteer, c for Cyborg')
        name = input('Please enter name of a worker')
        if a_type == 'd':
            workers.append(Dolphin(name))
        elif a_type == 'i':
            workers.append(Diver(name))
        elif a_type == 'v':
            workers.append(Volunteer(name))
        elif a_type == 'c':
            workers.append(Cyborg())
            print('Name of all cyborgs is IС1000 - rewriting')
        else:
            print('Incorrect input')


def enter_salary():

    global salary

    while True:
        try:
            salary = float(input('Enter salary: '))
            break
        except ValueError:
            print('Incorrect input. Please try again')


def work():

    global workers
    global salary

    # робота бригади
    for worker in workers:
        worker.pay(salary)
        print(worker)

    sum_general = []
    sum_hourly = []
    for i in range(1, 9):
        print(f'\thour {i}')
        for worker in workers:
            quantity = worker.work()
            sum_hourly.append(quantity)
            print(worker.name, f'{quantity:.2f}')
        s = sum(sum_hourly)
        sum_general.append(s)
        sum_hourly = []
        print(f'sum {s:.2f}')
        print()
    print(f'End of work. Number of vodorosli {sum(sum_general):.2f}')

    return sum(sum_general)


# menu()
#
# if workers:
#     print(workers)
#     work()
# else:
# print('There is no workers')


def generate_salary():
    global salary
    salary = random.randint(1, 300)
    print('salary', salary)


def generate_list_of_workers(num_of_workers):
    types = [Dolphin, Diver, Volunteer, Cyborg]

    with open('names.txt', 'r') as f:
        names = f.read().split('\n')

    for i in range(num_of_workers):
        # generating random type and name
        random_type = random.choice(types)
        random_name = random.choice(names)
        workers.append(random_type(random_name))

    for worker in workers:
        print(type(worker), worker)
    return workers


while True:
    try:
        n_of_workers = int(input('How many workers do you want to create?\n'))
        break
    except ValueError:
        print('Incorrect input. Please try again')

# generate_list_of_workers(num_of_workers)
# generate_salary()
# work()

num_of_tries = 30

d = {}

for i in range(num_of_tries):
    workers = generate_list_of_workers(n_of_workers)
    generate_salary()

    summa = work()
    d[summa] = workers
    workers = []

for summa, workers in d.items():
    print(f'{summa:.2f}', workers)
print()


# витащити кі велью пару з найбільшим кі і роздрукувати її

max_key = max(d.keys())
print(f'{max_key:.2f}', d[max_key])
