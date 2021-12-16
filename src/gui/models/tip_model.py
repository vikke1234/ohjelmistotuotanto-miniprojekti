from typing import Union
from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from PyQt5.QtGui import QColor, QBrush, QColorConstants


class TipModel(QAbstractListModel):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.__tips = []
        self.__displayed = []

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.__displayed)

    def append_item(self, item):
        """
        Appends a given item to the list view
        """
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__tips.append(item)
        self.__displayed = self.__tips
        self.endInsertRows()

    def mark_as_read(self, index):
        self.__tips[index.row()].read = True

    def insertRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
        self.beginInsertRows(parent, row, row + count)
        for _ in range(count):
            self.__tips.append(None)
        self.endInsertRows()

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            return

        row = index.row()

        if role == Qt.DisplayRole:
            tip = self.__displayed[row]
            return str(tip)

        if role == QtCore.Qt.UserRole:
            return self.__tips[row]

        if role == Qt.BackgroundRole:
            return QBrush(QColorConstants.Gray) if self.__tips[row].read else None

    def filter_by_tag(self, tag: str):
        # pretty inefficent way but currently the easiest
        self.__displayed = list(filter(lambda x: len([t for t in x.tags if t.startswith(tag)]) > 0, self.__tips))
        self.dataChanged.emit(QModelIndex(), QModelIndex())

