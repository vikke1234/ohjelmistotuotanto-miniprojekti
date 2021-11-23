import curses

class Tui:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        self.stdscr.addstr(0, 0, "Hello world")
        self.stdscr.refresh()
        self.stdscr.getkey()

    def destroy(self):
        curses.endwin()

