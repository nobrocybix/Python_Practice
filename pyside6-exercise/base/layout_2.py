import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QWidget,
    QComboBox
)

from layout_colorwidget import Color

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout 2")
        self.color1 = "red"
        self.color2 = "green"

        widget1 = QComboBox()
        widget1.addItems(["red", "blue", "green"])        
        widget1.setEditable(True)
        widget1.setInsertPolicy(QComboBox.InsertAtTop)
        widget1.currentTextChanged.connect(self.current_text_changed_1)
        widget1.editTextChanged.connect(self.edit_text_changed_1)

        widget2 = QComboBox()
        widget2.addItems(["red", "blue", "green"])
        widget2.setCurrentIndex(2)
        widget2.setEditable(True)
        widget1.setInsertPolicy(QComboBox.InsertAtTop)
        widget2.currentTextChanged.connect(self.current_text_changed_2)
        widget2.editTextChanged.connect(self.edit_text_changed_2)

        self.layout = QGridLayout()
        self.layout.addWidget(widget1, 0, 0)
        self.layout.addWidget(widget2, 1, 0)
        self.layout.addWidget(Color(self.color1), 0, 1)
        self.layout.addWidget(Color(self.color2), 1, 1)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def current_text_changed_1(self, s):
        self.layout.addWidget(Color(s), 0, 1)

    def current_text_changed_2(self, s):
        self.layout.addWidget(Color(s), 1, 1)

    def edit_text_changed_1(self, s):
        self.layout.addWidget(Color(s), 0, 1)

    def edit_text_changed_2(self, s):
        self.layout.addWidget(Color(s), 1, 1)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()