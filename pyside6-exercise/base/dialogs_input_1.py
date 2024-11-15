import sys, os

from PySide6.QtGui import QAction, QIcon, QKeySequence, Qt
from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QMainWindow,
)

basedir = os.path.dirname(__file__)
image_1 = os.path.join(basedir, "images", "calculator-gray.png")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialogs input")

        # Creat Menu
        menu = self.menuBar()
        data_menu = menu.addMenu("&輸入數據")

        # Button Action
        button_action = QAction(QIcon(image_1), "整數", self)
        button_action.triggered.connect(self.onMyToolBarButtonClick)      
        button_action.setShortcut(QKeySequence("Ctrl+i"))
        data_menu.addAction(button_action)
        
    def onMyToolBarButtonClick(self):
        my_int_value, ok = QInputDialog.getInt(
            self, "輸入一個整數", "獲得一個整數"
        )
        print("結果:", ok, my_int_value)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()