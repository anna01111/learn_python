""" Фінальний іспит"""
from maze_classes import *


def maze_controller(mr):
    # res = True
    # while res:
    #     res = mr.go()
    #     print(res)
    #
    # mr.turn_right()
    #
    # res = True
    # while res:
    #     res = mr.go()
    #     print(res)
    #
    # mr.turn_left()
    #
    # res = True
    # while res:
    #     res = mr.go()
    #     print(res)
    #
    # print(f'Found/NotFound {mr.found()}')

    # один шлях
    state = True
    while not mr.found():
        state = mr.go()
        if not state:
            mr.turn_right()







maze_example1 = {
    'm': [
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ],
    's': (0, 0),
    'f': (4, 4)
}


maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])  # ініціалізація робота
maze_controller(maze_runner)  # виклик вашої функції
# print(maze_runner.found())   # перевірка того, що артефакт знайдено, повинно бути True




