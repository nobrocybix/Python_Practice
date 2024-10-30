from PyQt6.QtWidgets import QApplication, QMainWindow

import sys

app = QApplication(sys.argv)

# in Qt any widgets can be windows
window = QMainWindow()
window.show()

app.exec()