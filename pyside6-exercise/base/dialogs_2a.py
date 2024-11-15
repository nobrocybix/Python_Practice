import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)

class CustomDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("你好")

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("發生了什麼事？")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialogs")

        button = QPushButton("按我")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, c):
        print(c)

        dlg = CustomDialog()
        if dlg.exec():
            print("成功!")
        else:
            print("取消!")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()