import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import(
    QApplication, QMainWindow, QFileDialog,
)

file_filters = [
    "Windows點陣圖(*.bmp)",
    "可攜式網路圖片(*.png)",
    "圖形交換格式(*.gif)",
    "聯合專家組(*..jpeg *.jpg)",
    "文字檔(*.txt)",
    "逗號分隔值(*.csv)",
    "所有檔案(*.*)",
]

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
        initial_filter = file_filters[4]
        filters = ";;".join(file_filters)
        file_name, selected_filter = QFileDialog.getOpenFileName(
                self,
                filter=filters,
                selectedFilter=initial_filter,
            )
        print("結果:", file_name, selected_filter)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()