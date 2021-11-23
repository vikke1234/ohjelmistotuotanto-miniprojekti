import curses
from curses.textpad import Textbox, rectangle


class TextEditError(Exception):
    pass

class TextEdit:
    """
    A simple single line text edit that can be used for search bars etc.
    """
    def __init__(self, stdscr, x: int, y: int, width: int = 30) -> None:
        """
        :param stdscr: window element
        :param x: x coordinate from where to create the text edit, required to be larger than 1
        :param y: y coordinate from where to create the text edit, required to be larger than 1
        :param width: width of the box
        """
        if x < 1 or y < 1:
            raise TextEditError("x and y need to be larger than 1")
        if x > curses.COLS - 1 or y > curses.LINES - 1:
            raise TextEditError(f"{x} > curses.COLS - 1 or {y} > curses.LINES - 1")

        rows = 1
        editwin = curses.newwin(rows, width, y, x)
        rectangle(stdscr, y-1, x-1, y + 1, x + width)

        stdscr.refresh()
        box = Textbox(editwin)
        box.edit(self._validator)

    @staticmethod
    def _validator(key) -> int:
        """
        This will convert movement etc. into movement keystrokes on the textbox,
        otherwise you'd need to use emacs bindings
        """
        # del aka backspace, does not exist in cpython for some reason
        if key == 127:
            return curses.KEY_BACKSPACE
        return key
