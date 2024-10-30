from PyQt6.QtWidgets import QApplication, QWidget

import sys

# Qapplications instance passing in sys.argv to allow the command line arguements for app.
app = QApplication(sys.argv)

# 
window = QWidget()

window.show()

app.exec()