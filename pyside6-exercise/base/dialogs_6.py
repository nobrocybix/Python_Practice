import sys

from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QVBoxLayout,
    QMainWindow, QWidget,
    QMessageBox, 
    QLineEdit, QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.num_input = ''

        self.setWindowTitle("Dialogs")

        # Layout
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout1.addLayout(layout2)

        # QLineEdit
        self.widget1 = QLineEdit()
        validator1 = QIntValidator()
        validator2 = QDoubleValidator()
        self.widget1.setValidator(validator1)
        self.widget1.setValidator(validator2)
        self.widget1.setPlaceholderText("請輸入想要的數字")
        self.widget1.setClearButtonEnabled(True)
        self.widget1.textEdited.connect(self.text_edited)
        self.widget1.returnPressed.connect(self.return_pressed)
        layout2.addWidget(self.widget1)

        # QPushButton
        widget2 = QPushButton("Enter")
        widget2.clicked.connect(self.button_clicked)
        layout2.addWidget(widget2)
        
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
    
    def text_edited(self, s):
        self.num_input = s

    def button_clicked(self, c): 
        self.show_dialog()

    def return_pressed(self):
        self.show_dialog()

    def show_dialog(self):
        
        if self.num_input == '':
            button = QMessageBox.warning(
                self,
                "注意",
                "請輸入數字"
            )
        else:
            button = QMessageBox.question(
                self, 
                "這是你想要的數字", 
                self.num_input,
                buttons = QMessageBox.Yes
                | QMessageBox.No
                | QMessageBox.Reset,
                defaultButton = QMessageBox.Yes
            )
     
            if button == QMessageBox.Reset:
                self.widget1.clear()
                self.widget1.setPlaceholderText("請輸入想要的數字")
            elif button == QMessageBox.No:
                self.widget1.clear()
                self.widget1.setPlaceholderText("請再輸入想要的數字")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()