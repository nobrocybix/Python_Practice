import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbars and menus")

        toolbar = QToolBar()
        toolbar.toggleViewAction().setEnabled(False)

        self.addToolBar(toolbar)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()