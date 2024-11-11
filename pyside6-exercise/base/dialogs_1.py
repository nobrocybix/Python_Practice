import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QPushButton,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialogs")

        button = QPushButton("按我")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, c):
        print(c)

        dlg = QDialog(self)
        dlg.setWindowTitle("你好")
        dlg.exec()



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()