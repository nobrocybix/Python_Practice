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
        dialog = QInputDialog(self)
        dialog.setWindowTitle("獲得一個整數")
        dialog.setLabelText("輸入一個整數")
        dialog.setIntValue(0)
        dialog.setIntMinimum(-10)
        dialog.setIntMaximum(10)
        dialog.setIntStep(1)

        ok = dialog.exec()
        print("結果:", ok, dialog.intValue())

    def get_a_float(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("獲得一個點數")
        dialog.setLabelText("輸入一個浮點數")
        dialog.setDoubleValue(0.1)
        dialog.setDoubleMinimum(-5.3)
        dialog.setDoubleMaximum(5.7)
        dialog.setDoubleStep(1.4)
        dialog.setDoubleDecimals(2)

        ok = dialog.exec()
        print("結果:", ok, dialog.doubleValue())

    def get_a_str_from_a_list(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("選擇一個字串")
        dialog.setLabelText("從清單中選擇一種水果")
        dialog.setComboBoxItems( ["蘋果","梨子","柳橙","葡萄"])
        dialog.setComboBoxEditable(False)
        dialog.setTextValue("柳橙")

        ok = dialog.exec()
        print("結果:", ok, dialog.textValue())

    def get_a_str(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("輸入字串")
        dialog.setLabelText("T輸入您的密碼")
        dialog.setTextValue("我的秘密密碼")
        dialog.setTextEchoMode(QLineEdit.EchoMode.Password)

        ok = dialog.exec()
        print("結果:", ok, dialog.textValue())

    def get_text(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("輸入文字")
        dialog.setLabelText("在這裡輸入您的小說")
        dialog.setTextValue("曾幾何時...")
        dialog.setOption(
            QInputDialog.UsePlainTextEditForTextInput,
            True,
        )

        ok = dialog.exec()
        print("結果:", ok, dialog.textValue())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()