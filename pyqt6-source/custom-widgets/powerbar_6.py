import sys

from PyQt6.QtCore import Qt, QSize, QRect, QRectF
from PyQt6.QtGui import QColor, QPainter, QBrush
from PyQt6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QApplication, QDial


class _Bar(QWidget):
    def __init__(self):
        super().__init__()

        self.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding,
            QSizePolicy.Policy.MinimumExpanding,
        )

    def sizeHint(self):
        return QSize(40, 120)

    def paintEvent(self, e):
        painter = QPainter(self)

        brush = QBrush()
        brush.setColor(QColor("black"))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
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

        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * 5)

        # tag::dimensions[]
        padding = 5

        # Define our canvas.
        d_height = painter.device().height() - (padding * 2)
        d_width = painter.device().width() - (padding * 2)
        # end::dimensions[]

        # tag::layout[]
        step_size = d_height / 5
        bar_height = step_size * 0.6
        # end::layout[]

        # tag::draw[]
        brush.setColor(QColor("red"))

        for n in range(n_steps_to_draw):
            ypos = (1 + n) * step_size
            rect = QRectF(
                padding,
                padding + d_height - int(ypos),
                d_width,
                bar_height,
            )
            painter.fillRect(rect, brush)
        # end::draw[]
        painter.end()

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
