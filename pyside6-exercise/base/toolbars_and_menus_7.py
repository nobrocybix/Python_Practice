import os
import sys

from random import randint

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication, QStackedLayout, QWidget,
    QMainWindow,
    QToolBar,
    QStatusBar,
    QLabel,
    QCheckBox
)
basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbars and menus")
        self.setMinimumSize(QSize(800, 600))

        # layout
        self.stacklayout = QStackedLayout()

        widget1 = QLabel()
        widget1.setPixmap(QPixmap(os.path.join(basedir, "images/01.jpg")))
        widget2 = QLabel()
        widget2.setPixmap(QPixmap(os.path.join(basedir, "images/02.jpg")))
        widget3 = QLabel()
        widget3.setPixmap(QPixmap(os.path.join(basedir, "images/03.png")))
        widget4 = QLabel()
        widget4.setPixmap(QPixmap(os.path.join(basedir, "images/04.png")))
        self.stacklayout.addWidget(widget1)
        self.stacklayout.addWidget(widget2)      
        self.stacklayout.addWidget(widget3)
        self.stacklayout.addWidget(widget4)

        toolbar = QToolBar("工具列")
        toolbar.setIconSize(QSize(24, 24))
        self.addToolBar(toolbar)

        # button_1
        button_action = QAction(
            QIcon(os.path.join(basedir, "images", "disk-return-black.png")),
            "disk", 
            self)
        button_action.setStatusTip("這是我的按鈕")
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        # button_2
        button_action2 = QAction(
            QIcon(os.path.join(basedir, "images", "animal.png")),
            "animal",
            self,
        )
        button_action2.setStatusTip("這是我的按鈕2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("喵"))
        
        # QCheckBox
        check_box1 = QCheckBox()
        toolbar.addWidget(check_box1)
        check_box1.checkStateChanged.connect(self.check_state1)

        
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("5000毫秒後自動消失", 5000)

        # menuBar
        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)

        widget = QWidget()
        widget.setLayout(self.stacklayout)
        self.setCentralWidget(widget)

    def onMyToolBarButtonClick(self, is_checked):
        print("click", is_checked)
        random_value = randint(1, 3)
        self.stacklayout.setCurrentIndex(random_value)
        if random_value == 1:
            self.statusBar().showMessage("狗")
        elif random_value == 2:
            self.statusBar().showMessage("企鵝")
        elif random_value == 3:
            self.statusBar().showMessage("海豚")

    def check_state1(self, s):
        if s == Qt.Checked:
            self.stacklayout.setCurrentIndex(0)
            self.statusBar().showMessage("貓")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()