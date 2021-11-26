import sys

from PyQt5.Qt import QApplication

from gui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec_()

if __name__ == "__main__":
    main()
