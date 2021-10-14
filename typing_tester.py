import random
import tkinter

from pynput.keyboard import Key

funny_mode = False


class TypingTester:

    def on_key_press(self, *args):
        if len(args[0].get()) > 0 and args[0].get()[-1] == ' ':
            self.input_entry.content.set('')
            if funny_mode:
                # reshuffle all the display words
                self.shuffle_display_words()
            else:
                # shift all the words to the left and add a new one on the right
                self.display_words.pop(0)
                self.display_words.append(''.join(random.sample(self.dictionary, 1)))
            self.update_display_word_labels()

    def put_empty_space(self, row, column):
        space = tkinter.Frame(self.ui_frame, width=self.padding, height=self.padding)
        space.grid(row=row, column=column)

    def shuffle_display_words(self):
        self.display_words = [''.join(random.sample(self.dictionary, 1)) for i in range(5)]

    def update_display_word_labels(self):
        for display_word_label in enumerate(self.display_word_labels):
            display_word_label[1].config(text=self.display_words[display_word_label[0]])

    def __init__(self, dictionary):

        self.padding = 25
        self.dictionary = dictionary
        total_display_words = 5

        self.ui = tkinter.Tk()
        self.ui_frame = tkinter.Frame(self.ui)
        self.ui_frame.pack()
        self.put_empty_space(0, 0)
        self.put_empty_space(0, 6)
        self.put_empty_space(6, 0)
        self.put_empty_space(6, 6)

        # heading
        instruction_text = tkinter.Label(self.ui_frame, text='Type the words you see')
        instruction_text.grid(row=1, column=3)

        self.put_empty_space(2, 3)

        # display words
        self.display_words_frame = tkinter.Frame(self.ui_frame)
        self.display_words_frame.grid(row=3, column=3)

        self.display_words = []
        self.shuffle_display_words()

        self.display_word_labels = [tkinter.Label(self.display_words_frame, text=display_word)
                                    for display_word in self.display_words]
        self.update_display_word_labels()

        print(self.display_word_labels)

        # todo - this is bad code and should be rewritten
        for display_word_label in enumerate(self.display_word_labels):
            display_word_label[1].grid(row=2, column=display_word_label[0])

        self.put_empty_space(4, 3)

        # entry content
        entry_content = tkinter.StringVar()
        entry_content.trace("w", lambda name, index, mode, content=entry_content: self.on_key_press(content))

        self.input_entry = tkinter.Entry(self.ui_frame, textvariable=entry_content)
        self.input_entry.content = entry_content
        self.input_entry.grid(row=5, column=3)

        """
        if funny_mode:
            # reshuffle all the display words
            self.shuffle_display_words()
        else:
            # shift all the words to the left and add a new one on the right
            self.display_word_labels.pop(0)
            self.display_word_labels.append(''.join(random.sample(self.dictionary, 1)))

        self.update_display_word_labels()

        """
        print(self.display_words)
        self.ui.mainloop()

        '''
        self.callback = self.on_key_press
        self.total_display_words = 5
        self.dictionary = dictionary
        self.display_word_frame = tkinter.Frame(self.ui_frame)
        self.display_word_frame.grid(row=3, column=2)
        self.display_word_labels = [self.add_label(
            ''.join(random.sample(self.dictionary, 1)),
            self.display_word_frame, 0, i + 1)
                                    for i in range(self.total_display_words)]
        self.add_label('Type the words you see', self.ui_frame, 1, 2)

        self.add_blank_space(2, 1, 100, 50)

        # self.set_display_words()

        self.add_blank_space(4, 1, 50, 50)

        self.input_entry = self.add_entry(5, 2)

        self.show()
        '''


'''
    def shift_display_words(self):
        self.display_words = random.sample(dictionary, 3)
        self.display_words_label.config(text=' '.join(self.display_words))
'''


def main():
    f = open('words.txt', 'r')
    test_interface = TypingTester(f.read().split('\n'))


if __name__ == '__main__':
    main()
