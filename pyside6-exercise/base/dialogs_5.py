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
        self.widget1.setClearButtonEnabled(True)
        self.widget1.textEdited.connect(self.text_edited)
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
        dlg = QMessageBox(self)
        dlg.setWindowTitle("This is you number")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        
        if self.num_input == '':
            message = "請輸入數字"
        else:
            message = self.num_input

        button = QMessageBox.question(
            self, "This is you number", message
        )
     
        if button == QMessageBox.No:
            self.widget1.clear()
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()