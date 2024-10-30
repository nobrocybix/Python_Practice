from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from random import choice
import sys

window_titles = [
    "不要再按",
    "再按一次",
    "這是一個按鈕",
    "今天天氣如何?",
    "你好",
    "早晨",
]
class MainWindow(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.setWindowTitle("這是視窗")
        self.default_checked = True
        
        self.button = QPushButton("按我")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.default_checked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setMinimumSize(QSize(400, 300))
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.window_title = choice(window_titles)
        self.setWindowTitle(self.window_title)
        self.button.setText(self.window_title)
        
    def the_window_title_changed(self, window_title):
        if window_title == "不要再按":
            self.button.setEnabled(False)
        
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()