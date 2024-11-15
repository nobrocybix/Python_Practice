import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import(
    QApplication, QMainWindow, QFileDialog,
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialogs File")

        file_action = QAction("開啟檔案...", self)
        file_action.setShortcut("Ctrl+O")
        file_action.triggered.connect(self.file_triggered)

        menu = self.menuBar()
        file_menu = menu.addMenu("&檔案")

        file_menu.addAction(file_action)

    def file_triggered(self):
        filters = "Images (*.png *.xpm *.jpg);;All File(*.*) "
        file_name, selected_filter = QFileDialog.getOpenFileName(
                self,
                filter=filters
            )
        print("結果:", file_name, selected_filter)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()