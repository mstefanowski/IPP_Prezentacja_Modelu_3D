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

    def narysuj_polygon(self, polygon, painter):
        d=80
        QPoint_list = []
        macierz_rzut = [
            [1, 0, 0, 0],
            [0, 1, 0, 0], 
            [0, 0, 1, 0], 
            [0, 0, 1/d, 0]]
        for punkt in polygon:
            x = punkt + [1]
            Zrzutowany_Punkt = self.normalizuj(self.matrix_vector_mult(macierz_rzut, x))
            QPoint_list.append(QPoint(Zrzutowany_Punkt[0], Zrzutowany_Punkt[1]))
        print(QPoint_list)
        painter.drawPolygon(QPolygon(QPoint_list))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.black)


        for polygon in self.obiekt3D:
            self.narysuj_polygon(polygon, painter)

    
        

    def wstaw_obiekt(self, obiekt3D):
        self.obiekt3D = obiekt3D