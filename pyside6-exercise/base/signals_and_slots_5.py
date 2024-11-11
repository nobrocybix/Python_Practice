import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget: Cube Numbers')

        self.widget = QListWidget()
        self.widget.addItems(self.cube_numbers())

        self.widget.currentItemChanged.connect(self.item_changed)
        self.widget.itemClicked.connect(self.item_clicked)
        self.widget.currentRowChanged.connect(self.row_changed)
        
        self.setCentralWidget(self.widget)

    def cube_numbers(self):
        cube_list = [str(x**3) for x in range(1, 11)]

        return cube_list

    def item_changed(self, i, p):
        print("current: " + i.text())
        if p is not None:
            print("previous: " + p.text())
    
    def item_clicked(self, i):
        print("*item: " + str(i))

    def row_changed(self, i):
        print("current row: " + str(i))
                     
app = QApplication(sys.argv)
window = Main()

window.show()
app.exec()