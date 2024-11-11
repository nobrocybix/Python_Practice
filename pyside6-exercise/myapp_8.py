import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSlider")
        self.setMinimumSize(QSize(200,800))

        widget = QSlider()

        widget.setRange(-500,500)
        widget.setValue(-100) 
        widget.setTickPosition(QSlider.TicksBothSides)
        widget.setSingleStep(10)
        widget.sliderMoved.connect(self.slider_position)

        self.setCentralWidget(widget)

    def slider_position(self, p):
        print("位置", p)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
