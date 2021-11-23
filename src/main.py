from curses import wrapper
from ui.tui import Tui

def main(stdscr):
    tui = Tui(stdscr)
    tui.hello_world()

if __name__ == "__main__":
    wrapper(main)
