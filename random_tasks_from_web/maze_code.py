""" Фінальний іспит"""
from maze_classes import *


def maze_controller(mr):
    # # один шлях
    # state = True
    #
    # print(f'x: {mr.x}, y: {mr.y}')
    #
    # counter = 0
    # while not mr.found():
    #
    #     print(f'x: {mr.x}, y: {mr.y}')
    #     state = mr.go()
    #     if not state and counter == 0:
    #         mr.turn_right()
    #         counter += 1
    #     elif not state and counter > 0:
    #         mr.turn_left()
    #         #mr.turn_left()
    #         counter = 0

    # другий шлях
    state = True

    print(f'x: {mr.x}, y: {mr.y}')

    counter = 0
    while not mr.found():

        print(f'x: {mr.x}, y: {mr.y}')
        state = mr.go()
        if not state and counter == 0:
            mr.turn_right()
            counter += 1
        elif not state and counter == 1:
            mr.turn_left()
            #mr.turn_left()
            counter = 0

    print(f'x: {mr.x}, y: {mr.y}, FINISH')


maze_example1 = {
    'm': [
        [0,0,0,0,0,0,0,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1],
        [0,0,0,0,0,1,0,1],
        [0,1,0,1,1,1,1,1],
        [1,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0],
    ],
    's': (7,7),
    'f': (0,0)
}


# maze_example1 = {
#     'm': [
#         [0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 0],
#         [0, 0, 0, 1, 0],
#     ],
#     's': (0, 0),
#     'f': (4, 4)
# }


maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])  # ініціалізація робота
maze_controller(maze_runner)  # виклик вашої функції
# print(maze_runner.found())   # перевірка того, що артефакт знайдено, повинно бути True




