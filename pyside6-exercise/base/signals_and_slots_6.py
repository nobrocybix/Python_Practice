import sys

from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow

class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit")

        widget = QLineEdit()
        widget.setClearButtonEnabled(True)
        widget.setMaxLength(15)
        widget.setPlaceholderText("請輸入")
        
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed")
        self.centralWidget().setText("輸入完成")
    
    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)
            
app = QApplication(sys.argv)

window = Main()
window.show()

app.exec()