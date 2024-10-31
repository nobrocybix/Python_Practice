from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize, Qt
import sys

class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input")
        self.setMinimumSize(QSize(800,400))

        self.label = QLabel()
        
        self.message = QLabel("輸入")
        m_font = self.message.font()
        m_font.setPointSize(30)
        

        font = self.label.font()
        font.setPointSize(30)
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)

        self.message.setFont(font)

        self.label.setPixmap(QPixmap("D:/temp/pic/image.jpeg"))
        self.label.setScaledContents(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignJustify | Qt.AlignmentFlag.AlignTop)

        self.input = QLineEdit()
        self.input.setFixedSize(QSize(100, 30))
        self.input.textChanged.connect(self.label.setText)
        
        layout = QVBoxLayout()
        layout.addWidget(self.message)
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
    

app = QApplication(sys.argv)

window = Main()
window.show()

app.exec()