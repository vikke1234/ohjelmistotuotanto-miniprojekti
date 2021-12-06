from typing import Union
from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt


class TipModel(QAbstractListModel):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.__tips = []

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.__tips)

    def append_item(self, item):
        """
        Appends a given item to the list view
        """
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__tips.append(item)
        self.endInsertRows()

    def insertRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
        self.beginInsertRows(parent, row, row + count)
        for _ in range(count):
            self.__tips.append(None)
        self.endInsertRows()

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            return

        if role == Qt.DisplayRole:
            row = index.row()
            s = ""
            for k, v in self.__tips[row].items():
                if v != "":
                    s += f"{k}: {v}\n"
            return s

