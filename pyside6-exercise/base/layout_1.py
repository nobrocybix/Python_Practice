import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QWidget
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")
        self.setMaximumSize(QSize(230, 100))
        self.num_input = ''

        widget1 = QLabel()
        widget1.setText("**請輸入數字**")
        font = widget1.font()
        font.setPointSize(15)
        widget1.setFont(font)
        widget1.setTextFormat(Qt.MarkdownText)
        widget1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)


        widget2 = QLineEdit()
        widget2.setMaxLength(10)
        widget2.setPlaceholderText("number only")
        # 設置驗證器，只允許輸入整數
        validator = QIntValidator()  
        widget2.setValidator(validator)     
        widget2.setClearButtonEnabled(True)
        widget2.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        widget2.textEdited.connect(self.text_edited)
        widget2.returnPressed.connect(self.return_pressed)
        widget2.textChanged.connect(self.text_changed)

        widget3 = QPushButton("Enter")
        widget3.clicked.connect(self.the_button_was_clicked)

        self.widget4 = QLabel()
        self.widget4.setFont(font)
        self.widget4.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout1.addWidget(widget1)
        layout2.addWidget(widget2)
        layout2.addWidget(widget3)
        layout1.addLayout(layout2)
        layout1.addWidget(self.widget4)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    
    def text_edited(self, s):
        self.num_input = s
    
    def return_pressed(self):
        self.widget4.setText(self.num_input)

    def text_changed(self, s):
        if s == '':
            self.widget4.setText('')

    def the_button_was_clicked(self):
        self.widget4.setText(self.num_input)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()