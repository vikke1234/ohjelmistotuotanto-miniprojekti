from PyQt5 import QtGui
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QLineEdit, QListWidgetItem, QMainWindow, QWidget

from gui.components.mainwindow import Ui_MainWindow
from gui.models.tip_model import TipModel

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main window class
    """
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.add_button.clicked.connect(self.add_to_list)
        self.listView.setModel(TipModel(self))

    def add_to_list(self):
        """
        Adds the content of the url line edit to the saved tips list
        """
        current: QWidget = self.input_form.currentWidget()
        if current is None:
            return
        layout = current.layout()
        if layout is None:
            return

        item = {}
        for row in range(layout.count()):
            label = layout.itemAt(row, 0)
            line_edit = layout.itemAt(row, 1)
            if label is not None and line_edit is not None:
                item[label.widget().text().lower()] = line_edit.widget().text()
        self.listView.model().append_item(item)

