from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QCheckBox
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
        self.pixmap_image = QLabel()
        widget = QCheckBox("clear")
        widget.setCheckState(Qt.CheckState.Unchecked)
        widget.setTristate(True)
    
        font = self.label.font()
        font.setPointSize(30)
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        self.message.setFont(font)
        self.label.setFont(font)

        self.pixmap_image.setPixmap(QPixmap("D:/temp/pic/image.jpeg"))
        self.pixmap_image.setScaledContents(True)
        self.pixmap_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input = QLineEdit()
        self.input.setFixedSize(QSize(100, 30))
        self.input.textChanged.connect(self.label.setText)
        widget.checkStateChanged.connect(self.label.clear)
        
        layout = QVBoxLayout()
        layout.addWidget(widget)
        layout.addWidget(self.message)
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.pixmap_image)

        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
    
 
    

app = QApplication(sys.argv)

window = Main()
window.show()

app.exec()