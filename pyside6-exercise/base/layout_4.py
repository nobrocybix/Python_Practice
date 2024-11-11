import os
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QLabel
)


basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout 4")
        self.setMinimumSize(QSize(800, 600))

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        widget1 = QLabel()
        widget1.setPixmap(QPixmap(os.path.join(basedir, "images/01.jpg")))
        widget2 = QLabel()
        widget2.setPixmap(QPixmap(os.path.join(basedir, "images/02.jpg")))
        widget3 = QLabel()
        widget3.setPixmap(QPixmap(os.path.join(basedir, "images/03.png")))
        widget4 = QLabel()
        widget4.setPixmap(QPixmap(os.path.join(basedir, "images/04.png")))
        
        tabs.addTab(widget1, '貓')
        tabs.addTab(widget2, "狗")
        tabs.addTab(widget3, "企鵝")
        tabs.addTab(widget4, "海豚")

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()