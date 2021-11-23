from curses import wrapper
from ui.tui import Tui

def main(stdscr):
    tui = Tui(stdscr)

if __name__ == "__main__":
    wrapper(main)
