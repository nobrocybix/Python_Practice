import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QCheckBox

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
    
        widget = QCheckBox()
        widget.setText("CheckBox")
        widget.setTristate(True)
        widget.setCheckState(Qt.CheckState.Unchecked)

        widget.checkStateChanged.connect(self.checked)

        self.setCentralWidget(widget)

    def checked(self, s):
        print(s)
        print(Qt.CheckState(s))
        

app = QApplication(sys.argv)
window = Main()

window.show()
app.exec()
