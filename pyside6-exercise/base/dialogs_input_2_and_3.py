import sys, os

from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QLineEdit,
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
        data_menu = menu.addMenu(QIcon(image_1), "&輸入數據")

        # Button Action
        button_action = QAction("整數", self)
        button_action.triggered.connect(self.get_an_int)
        button_action.setShortcut(QKeySequence("Ctrl+i"))
        data_menu.addAction(button_action)

        button_action2 = QAction("浮點數", self)
        button_action2.triggered.connect(self.get_a_float)
        button_action2.setShortcut(QKeySequence("Ctrl+f"))
        data_menu.addAction(button_action2)

        button_action3 = QAction("選擇", self)
        button_action3.triggered.connect(self.get_a_str_from_a_list)
        button_action3.setShortcut(QKeySequence("Ctrl+l"))
        data_menu.addAction(button_action3)   

        button_action4 = QAction("字串", self)
        button_action4.triggered.connect(self.get_a_str)
        button_action4.setShortcut(QKeySequence("Ctrl+s"))
        data_menu.addAction(button_action4)

        button_action5 = QAction("文字", self)
        button_action5.triggered.connect(self.get_text)
        button_action5.setShortcut(QKeySequence("Ctrl+t"))
        data_menu.addAction(button_action5)
                       
    def get_an_int(self):
        title = "獲得一個整數"
        label = "輸入一個整數"
        my_int_value, ok = QInputDialog.getInt(
            self, 
            title, 
            label,
            value=0,
            minValue=-10,
            maxValue=10,
            step=2,
        )
        print("結果:", ok, my_int_value)

    def get_a_float(self):
        title = "獲得一個整數"
        lable = "輸入一個浮點數"
        my_foat_value, ok = QInputDialog.getDouble(
            self,
            title,
            lable,
            value=0,
            minValue=-10.5,
            maxValue=10.5,
            decimals=3,
            step=1.555,
        )
        print("結果:", ok, my_foat_value)

    def get_a_str_from_a_list(self):
        title = "選擇一個字串"
        lable = "從清單中選擇一種水果"
        items = ["蘋果","梨子","柳橙","葡萄"]
        init = 3
        my_selected_str, ok = QInputDialog.getItem(
            self,
            title,
            lable,
            items,
            current=init,
            editable=False,
        )
        print("結果:", ok, my_selected_str)

    def get_a_str(self):
        title = "輸入字串"
        label ="輸入您的密碼"
        text = "我的秘密密碼"
        mode = QLineEdit.EchoMode.Password
        my_selected_str, ok = QInputDialog.getText(
            self, title, label, mode, text
        )
        print("結果:", ok, my_selected_str)
    
    def get_text(self):
        title = "輸入文字"
        label = "在這裡輸入您的小說"
        text = "曾幾何時..."
        my_selected_str, ok = QInputDialog.getMultiLineText(
            self, title, label, text
        )
        print("結果", ok, my_selected_str)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()