import curses
from typing import Union


class Scrollable:
    def __init__(self, stdscr, start_y: int, data: Union[list, None] = None) -> None:
        """
        :param start_y: from where to start drawing the area
        :param data: data to initialize list with
        """
        if data == None:
            self.data = []
        else:
            self.data = data.copy()
        self.stdscr = stdscr
        self.start_y = start_y
        self.current_y = 0

    def append_data(self, item) -> None:
        """
        Appends data to the list

        :param item: item to add to list """
        self.data.append(item)

    def display(self) -> None:
        """
        Displays the content of the content

        NOTE: the data in the list needs to have a __str__ function,
              other than that it doesn't care what type it is
        """
        first = self.current_y
        last = first + curses.LINES - self.start_y  # offset to fit however much should fit before the list

        for index, item in enumerate(self.data[first:last]):
            self.stdscr.addstr(1, 0, str(first))
            self.stdscr.addstr(2, 0, str(last))

            self.stdscr.addstr(self.start_y + index, 0, str(item))
            self.stdscr.refresh()

    def scroll(self, direction: int) -> None:
        """
        Scroll in a given direction

        :param direction: direction to scroll, needs to be either curses.KEY_UP or curses.KEY_DOWN
        """
        if direction == curses.KEY_DOWN:
            # make sure that we don't go all the way to the end of the list, otherwise
            # the console will be spammed with the last item
            self.current_y = min(self.current_y + 1, len(self.data) - (curses.LINES - self.start_y))
        elif direction == curses.KEY_UP:
            self.current_y = max(self.current_y - 1, 0)

