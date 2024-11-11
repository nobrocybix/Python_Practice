import os
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
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

        toolbar = QToolBar("工具列")
        toolbar.setIconSize(QSize(24, 24))
        self.addToolBar(toolbar)

        button_action = QAction(
            QIcon(os.path.join(basedir, "images", "disk-return-black.png")),
            "disk", 
            self)
        button_action.setStatusTip("這是我的按鈕")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(
            QIcon(os.path.join(basedir, "images", "animal.png")),
            "animal",
            self,
        )
        button_action2.setStatusTip("這是我的按鈕2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("喵"))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("5000毫秒後自動消失", 5000)

    def onMyToolBarButtonClick(self, is_checked):
        print("click", is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()