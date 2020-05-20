from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *


class Widget_rysowania(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.red)

        painter.drawLine(10,10,100,140)

        painter.setPen(Qt.blue)
        painter.drawRect(120,10,80,80)

        rectf = QRectF(230.0,10.0,80.0,80.0)
        painter.drawRoundedRect(rectf,20,20)

        p1 = [QPoint(10,100),QPoint(220,110),QPoint(220,190)]
        painter.drawPolyline(QPolygon(p1))

        p2 = [QPoint(120,110),QPoint(220,110),QPoint(220,190)]
        painter.drawPolygon(QPolygon(p2))