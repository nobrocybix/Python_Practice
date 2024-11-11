import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDoubleSpinBox")

        widget = QDoubleSpinBox()

        widget.setRange(0, 1000)

        widget.setPrefix("$")
        widget.setSingleStep(10)
        widget.textChanged.connect(self.value_changed)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()