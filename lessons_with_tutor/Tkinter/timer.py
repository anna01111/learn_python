from threading import Timer
from time import sleep


def hello():
    print("Hello user!")


def bye():
    sleep(2)
    print("Bye...bye...")


while 1:
    timer = Timer(300, hello)
    timer.start()
    bye()


