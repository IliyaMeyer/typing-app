import time
import copy
from typing_tester import TypingTester
from keylogger import Keylogger
from pynput.keyboard import Key, Listener

view_screen = TypingTester()


def get_average_difference(key_list):
    dif = 0
    for i in range(len(key_list) - 1):
        dif += key_list[i + 1][1] - key_list[i][1]
    return dif / (len(key_list) - 1)


def main():

    view_screen.show()


if __name__ == '__main__':
    main()
