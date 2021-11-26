from PyQt5.Qt import QMainWindow
from PyQt5.QtWidgets import QListWidgetItem

from gui.components.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.add_button.clicked.connect(self.add_to_list)

    def add_to_list(self):
        text = self.url_lineedit.text()
        item = QListWidgetItem()
        item.setText(text)
        current = self.listWidget.count()
        self.listWidget.insertItem(current+1, item)
