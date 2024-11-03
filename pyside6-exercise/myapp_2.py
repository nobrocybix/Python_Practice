from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt, QSize

import sys

class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLable")
        self.setMinimumSize(QSize(400, 200))

        self.widget = QLabel()
        self.widget.setText('<a href="https://doc.qt.io/qt-6/qlabel.html">QLabel</a>')
        self.widget.setOpenExternalLinks(True) # 允許外部鏈結被打開
        self.font = self.widget.font()
        self.font.setPointSize(30)
        self.widget.setFont(self.font)
        
        self.widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.widget)


app = QApplication(sys.argv)

window = Main()
window.show()

app.exec()
