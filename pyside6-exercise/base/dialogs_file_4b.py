import sys, os

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QKeySequence, QPixmap
from PySide6.QtWidgets import(
    QApplication, QMainWindow, QFileDialog, QLabel,
    QScrollBar, QMessageBox,
)

file_filters = [
    "Windows點陣圖(*.bmp)",
    "可攜式網路圖片(*.png)",
    "圖形交換格式(*.gif)",
    "聯合專家組(*.jpeg *.jpg)",
    "文字檔(*.txt)",
    "逗號分隔值(*.csv)",
    "所有檔案(*.*)",
]

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialogs File")
        self.label = QLabel()
        font = self.label.font()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(
            Qt.AlignLeft
            | Qt.AlignTop
        )
        self.label.setWordWrap(True)

        self.scroll_bar = QScrollBar(self)

        file_action = QAction("開啟檔案...", self)
        file_action.setShortcut(QKeySequence.Open)
        file_action.triggered.connect(self.get_filename)

        file_action2 = QAction("開啟多個檔案...", self)
        file_action2.setShortcut("Ctrl+A")
        file_action2.triggered.connect(self.get_filenames)

        file_action3 = QAction("另存新檔...", self)
        file_action3.setShortcut(QKeySequence.SaveAs)
        file_action3.triggered.connect(self.get_save_filename)

        file_action4 = QAction("開啟資料夾...", self)
        file_action4.setShortcut(QKeySequence(Qt.CTRL | Qt.Key_K, Qt.CTRL | Qt.Key_O))
        file_action4.triggered.connect(self.get_folder)
 
        menu = self.menuBar()
        file_menu = menu.addMenu("&檔案")

        file_menu.addAction(file_action)
        file_menu.addAction(file_action2)
        file_menu.addAction(file_action3)
        file_menu.addAction(file_action4)

        self.setCentralWidget(self.label)

    def get_filename(self):
        caption = ""
        initial_dir = ""
        initial_filter = file_filters[6]
        filters = ";;".join(file_filters)
        print("過濾器:", filters)
        print("初始過濾器:", initial_filter)

        file_name, selected_filter = QFileDialog.getOpenFileName(
                self,
                caption=caption,
                dir=initial_dir,
                filter=filters,
                selectedFilter=initial_filter,
            )
        print("結果:", file_name, selected_filter)

        _, ext = os.path.splitext(file_name)

        if ext.lower() == '.txt':
            with open(file_name, 'r') as f:
                file_contents = f.read()
                self.label.setText(file_contents)
        elif ext.lower() in ['.bmp', '.png', '.gif', '.jpeg', '.jpg']:
                self.label.setPixmap(QPixmap(file_name))

    def get_filenames(self):
        caption = ""  
        initial_dir = ""  
        initial_filter = file_filters[4] 
        filters = ";;".join(file_filters)
        print("過濾器:", filters)
        print("初始過濾器:", initial_filter)

        filenames, selected_filter = QFileDialog.getOpenFileNames(
            self,
            caption=caption,
            dir=initial_dir,
            filter=filters,
            selectedFilter=initial_filter,
        )
        print("結果:", filenames, selected_filter)

        combined_contents = ""
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext.lower() == '.txt':
                with open(filename, 'r') as f:
                    combined_contents += f.read()
            print(combined_contents)

    def get_save_filename(self):
        caption = ""  
        initial_dir = ""  
        initial_filter = file_filters[4] 
        filters = ";;".join(file_filters)
        print("過濾器:", filters)
        print("初始過濾器:", initial_filter)

        filename, selected_filter = QFileDialog.getSaveFileName(
            self,
            caption=caption,
            dir=initial_dir,
            filter=filters,
            selectedFilter=initial_filter,
        )
        print("結果:", filename, selected_filter)

        if filename:
            if os.path.exists(filename):
                # Existing file, ask for the user for confirmation.
                write_confirmed = QMessageBox.question(
                    self,
                    "覆蓋文件？",
                    f"檔案 {filename} 存在。您確定要覆蓋它嗎？",
                )
            else:
                # File does not exist, always-confirmed.
                write_confirmed = True

            if write_confirmed:
                with open(filename, "w") as f:
                    file_content = "您的文件內容"
                    f.write(file_content)


    def get_folder(self):
        caption = ""  
        initial_dir = ""  
        folder_path = QFileDialog.getExistingDirectory(
            self,
            caption=caption,
            dir=initial_dir,
        )
        print("結果:", folder_path)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()