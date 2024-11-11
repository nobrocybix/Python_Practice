import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QCheckBox

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
    
        widget = QCheckBox()
        widget.setText("CheckBox")
        widget.setTristate(True)
        widget.setCheckState(Qt.CheckState.Unchecked)

        widget.checkStateChanged.connect(self.check_state)

        self.setCentralWidget(widget)

    def check_state(self, s):
        
        print(s)
        print(Qt.CheckState(s))
        
        if s == Qt.Checked:
            print("----Checked----")
        elif s == Qt.Unchecked:
            print("----Unchecked----")
        elif s == Qt.PartiallyChecked:
            print("----PartiallyChecked----")
        

app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()