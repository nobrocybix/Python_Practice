import os
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QLabel
)

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout 3")
        self.setMinimumSize(QSize(800, 400))

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        widget1 = QLabel()
        widget1.setPixmap(QPixmap(os.path.join(basedir, "images/01.jpg")))
        widget2 = QLabel()
        widget2.setPixmap(QPixmap(os.path.join(basedir, "images/02.jpg")))
        widget3 = QLabel()
        widget3.setPixmap(QPixmap(os.path.join(basedir, "images/03.png")))
        widget4 = QLabel()
        widget4.setPixmap(QPixmap(os.path.join(basedir, "images/04.png")))

        btn = QPushButton("貓")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(widget1)

        btn = QPushButton("狗")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(widget2)

        btn = QPushButton("企鵝")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(widget3)

        btn = QPushButton("海豚")
        btn.pressed.connect(self.activate_tab_4)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(widget4)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)

    def activate_tab_4(self):
        self.stacklayout.setCurrentIndex(3)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

