from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, QModelIndex, QObject, QUrl
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
        self.tag_line.textChanged.connect(self.listView.model().filter_by_tag)

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
        self.listView.doubleClicked.connect(self.list_double_clicked)

    def list_double_clicked(self, index):
        model = self.listView.model()
        data = model.data(index, QtCore.Qt.UserRole)
        if hasattr(data, "url"):
            QtGui.QDesktopServices.openUrl(QUrl(data.url))
            model.mark_as_read(index)
