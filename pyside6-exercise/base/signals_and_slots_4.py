import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        
        self.widget = QComboBox()
        self.widget.addItems(["一", "二", "三", "四"])
        self.widget.setEditable(True)
        
        self.widget.currentIndexChanged.connect(self.combobox_changed)

        self.setCentralWidget(self.widget)

    def combobox_changed(self, s):
    
        print(self.widget.itemText(s))

                

app = QApplication(sys.argv)

window = Main()
window.show()

app.exec()