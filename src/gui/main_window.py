from PyQt5.QtWidgets import QListWidgetItem, QMainWindow

from gui.components.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main window class
    """
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.add_button.clicked.connect(self.add_to_list)

    def add_to_list(self):
        """
        Adds the content of the url line edit to the saved tips list
        """
        text = self.titleLineEdit.text() + " - " + self.linkLineEdit.text()
        item = QListWidgetItem()
        item.setText(text)
        current = self.listWidget.count()
        self.listWidget.insertItem(current+1, item)
        self.titleLineEdit.setText("")
        self.linkLineEdit.setText("")
