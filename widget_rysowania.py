from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *


class Widget_rysowania(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.przesuniecie_x = 0 
        self.przesuniecie_y = 0 
        self.przesuniecie_z = 0

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

    def matmult(self, m1,m2):
        r=[]
        m=[]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                sums=0
                for k in range(len(m2)):
                    sums=sums+(m1[i][k]*m2[k][j])
                r.append(sums)
            m.append(r)
            r=[]
        return m

    def normalizuj(self, vektor):
        vektor = [element / vektor[-1] for element in vektor]
        return vektor

    def stworz_macierz_przesuniecia(self, x, y, z):
        return [[1, 0, 0, x], 
                [0, 1, 0, y], 
                [0, 0, 1, z], 
                [0, 0, 0, 1]]

    def stworz_macierz_rzutu(self, d):
        return [
                [1, 0, 0, 0],
                [0, 1, 0, 0], 
                [0, 0, 1, 0], 
                [0, 0, 1/d, 0]]

    def narysuj_polygon(self, polygon, painter):
        d=80
        QPoint_list = []
        macierz_rzut = self.stworz_macierz_rzutu(d)
        macierz_przesuniecia = self.stworz_macierz_przesuniecia(self.przesuniecie_x, self.przesuniecie_y, self.przesuniecie_z)
        macierz_przeksztalcen = self.matmult(macierz_rzut, macierz_przesuniecia)
        for punkt in polygon:
            x = punkt + [1]
            Zrzutowany_Punkt = self.normalizuj(self.matrix_vector_mult(macierz_przeksztalcen, x))
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

    def przesun(self, x, y, z):
        self.przesuniecie_x = x 
        self.przesuniecie_y = y 
        self.przesuniecie_z = z

