"""
indexing for row's/column's with regards to the grid positions on the interface starts at 1
"""

import tkinter


class UserInterface:

    def __position_widget(self, widget, row, column):
        widget.grid(row=row, column=column)

    def callback(self, *args):
        print(args)

    def __init__(self, rows, columns, padding):
        # todo - refactor this block
        padding = padding
        horizontal_cells = rows + 2
        vertical_cells = columns + 2

        self.ui = tkinter.Tk()
        self.ui_frame = tkinter.Frame(self.ui)
        self.ui_frame.pack()
        self.ui.paddings = []
        for i in range(2):
            new_padding = tkinter.Frame(self.ui_frame)
            self.__position_widget(new_padding, i * (horizontal_cells - 1), i * (vertical_cells - 1))
            self.ui.paddings.append(new_padding)
        self.set_padding(padding)

    def show(self):
        self.ui.mainloop()

    def get_grid_size(self):
        return self.ui_frame.grid_size()

    def add_label(self, text, master, row, column):
        new_label = tkinter.Label(master, text=text, bg='green')
        self.__position_widget(new_label, row, column)
        return new_label

    def add_entry(self, row, column):
        entry_content = tkinter.StringVar()
        entry_content.trace("w", lambda name, index, mode, content=entry_content: self.callback(content, name))
        new_entry = tkinter.Entry(self.ui_frame, textvariable=entry_content)
        new_entry.variable = entry_content
        self.__position_widget(new_entry, row, column)
        return new_entry

    def add_blank_space(self, row, column, width, height):
        new_space = tkinter.Frame(self.ui_frame, width=width, height=height)
        self.__position_widget(new_space, row, column)
        return new_space

    def set_padding(self, padding_value, widget=None):
        if widget is None:
            widget = self.ui
        for padding in widget.paddings:
            padding.config(width=padding_value)
            padding.config(height=padding_value)


def main():
    pass

if __name__ == '__main__':
    main()
