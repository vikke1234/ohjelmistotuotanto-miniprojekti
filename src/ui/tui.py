import curses

class Tui:
    """
    Class to show TUI
    """

    def __init__(self, stdscr) -> None:
        """
        :stdscr: screen object from curses.initscr()
        """
        self.stdscr = stdscr
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)

    def hello_world(self):
        self.stdscr.addstr(0, 0, "Hello world")
        self.stdscr.refresh()
        self.stdscr.getkey()
