from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, QModelIndex, QObject
from PyQt5.QtWidgets import QLineEdit, QListWidgetItem, QMainWindow, QMenu, QWidget

from core.types import Book, Podcast, Video, BlogPost
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
        self.listView.installEventFilter(self)

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
        types = {
                0: Book,
                1: Podcast,
                2: Video,
                3: BlogPost
            }


        item_dict = {}
        for row in range(layout.count()):
            label = layout.itemAt(row, 0)
            line_edit = layout.itemAt(row, 1)
            if label is not None and line_edit is not None:
                item_dict[label.widget().text().lower()] = line_edit.widget().text()

        index = self.typeComboBox.currentIndex()
        item = types[index](**item_dict)
        self.listView.model().append_item(item)

    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        if event.type() == QtCore.QEvent.ContextMenu and source is self.listView:
            menu = QMenu()
            print("here")
            menu.addAction("Mark as read")
            if menu.exec_(event.globalPos()):
                print(event.pos())
        return super().eventFilter(source, event)
