import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QStatusBar
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbars and menus")

        toolbar = QToolBar("工具列")
        self.addToolBar(toolbar)

        button_action = QAction("按我", self)
        button_action.setStatusTip("這是我的按鈕")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("5000毫秒後自動", 5000)

    def onMyToolBarButtonClick(self, is_checked):
        print("click", is_checked)
        self.statusBar().showMessage("5000毫秒後自動", 5000)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()