from PyQt5.QtCore import qrand
import pytest
import pytestqt
from gui.main_window import MainWindow


def test_label2(qtbot):
    test_app = MainWindow()
    qtbot.addWidget(test_app)
    assert   "Choose the type to add" in test_app.label_2.text()

def test_combo_box_default_value(qtbot):
    test_app = MainWindow()
    qtbot.addWidget(test_app)
    assert test_app.typeComboBox.currentIndex() == 0 and test_app.typeComboBox.currentText() == "Book"

def test_default_lables(qtbot):
    test_app = MainWindow()
    qtbot.addWidget(test_app)
    assert test_app.nameLabel.text() == "Author"
    assert test_app.titleLabel.text() == "Title"
    assert test_app.iSBNLabel.text() == "ISBN"
    assert test_app.linkLabel.text() == "Tags"
    assert test_app.commentLabel.text() == "Comment"

def test_combo_box_value_changes(qtbot):
    test_app = MainWindow()
    qtbot.addWidget(test_app)
    qtbot.keyClicks(test_app.typeComboBox, "Podcast")
    assert test_app.typeComboBox.currentIndex() == 1 and test_app.typeComboBox.currentText() == "Podcast"

def test_labels_changes(qtbot):
    test_app = MainWindow()
    qtbot.addWidget(test_app)
    qtbot.keyClicks(test_app.typeComboBox, "Video")
    assert test_app.titleLabel_3.text() == "Title"
    assert test_app.iSBNLabel_3.text() == "URL"
    assert test_app.tagsLabel.text() == "Tags"
    assert test_app.commentLabel_3.text() == "Comment"

def test_add_button(qtbot):
    test_app = MainWindow()
