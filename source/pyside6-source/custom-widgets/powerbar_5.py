import sys

from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtGui import QColor, QPainter, QBrush
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QApplication, QDial



class _Bar(QWidget):
    def __init__(self):
        super().__init__()

        self.setSizePolicy(
            QSizePolicy.MinimumExpanding,
            QSizePolicy.MinimumExpanding,
        )

    def sizeHint(self):
        return QSize(40, 120)

    # tag::paintEvent[]
    def paintEvent(self, e):
        painter = QPainter(self)

        brush = QBrush()
        brush.setColor(QColor("black"))
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(
            0,
            0,
            painter.device().width(),
            painter.device().height(),
        )
        painter.fillRect(rect, brush)

        # Get current state.
        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pen = painter.pen()
        pen.setColor(QColor("red"))
        painter.setPen(pen)

        font = painter.font()
        font.setFamily("Times")
        font.setPointSize(18)
        painter.setFont(font)

        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * 5)
        painter.drawText(25, 25, "{}".format(n_steps_to_draw))
        painter.end()

    # end::paintEvent[]

    def _trigger_refresh(self):
        self.update()


class PowerBar(QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, parent=None, steps=5):
        super().__init__(parent)

        layout = QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        self._dial = QDial()
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = PowerBar()
window.show()
app.exec()
