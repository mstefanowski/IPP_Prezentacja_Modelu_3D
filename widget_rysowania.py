from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *


class Widget_rysowania(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def matrix_vector_mult(self, m, v):
        vektor = []
        if len(m) != len(v):
            raise Exception ("Wektor nie pasuje do macierzy")
        for i in range(len(m)):
            sum = 0
            for j in range(len(v)):
                sum = sum + m[i][j] * v[j]
            vektor.append(sum)
        return vektor

    def normalizuj(self, vektor):
        vektor = [element / vektor[-1] for element in vektor]
        return vektor

    def narysuj_polygon(self, polygon):
        d=1
        macierz_rzut = [
            [1, 0, 0, 0],
            [0, 1, 0, 0], 
            [0, 0, 1, 0], 
            [0, 0, 1/d, 0]]
        for punkt in polygon:
            x = punkt + [1]
            print(self.normalizuj(self.matrix_vector_mult(macierz_rzut, x)))

    def paintEvent(self, event):
        # painter = QPainter(self)
        # painter.setPen(Qt.red)

        # painter.drawLine(10,10,100,140)

        # painter.setPen(Qt.blue)
        # painter.drawRect(120,10,80,80)

        # rectf = QRectF(230.0,10.0,80.0,80.0)
        # painter.drawRoundedRect(rectf,20,20)

        # p1 = [QPoint(10,100),QPoint(220,110),QPoint(220,190)]
        # painter.drawPolyline(QPolygon(p1))

        # p2 = [QPoint(120,110),QPoint(220,110),QPoint(220,190)]
        # painter.drawPolygon(QPolygon(p2))

        for polygon in self.obiekt3D:
            self.narysuj_polygon(polygon)

    
        

    def wstaw_obiekt(self, obiekt3D):
        self.obiekt3D = obiekt3D