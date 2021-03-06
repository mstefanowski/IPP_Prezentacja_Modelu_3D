# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from widget_rysowania import Widget_rysowania
from file_loader import file_loader


class Ui_MainWindow(QMainWindow):
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(708, 496)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_pozycja_kamery = QtWidgets.QLabel(self.centralwidget)
        self.label_pozycja_kamery.setGeometry(QtCore.QRect(40, 20, 111, 17))
        self.label_pozycja_kamery.setObjectName("label_pozycja_kamery")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_pozycja_kamery = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_pozycja_kamery.setContentsMargins(0, 0, 0, 0)
        self.layout_pozycja_kamery.setObjectName("layout_pozycja_kamery")


        self.kamera_x = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.kamera_x.setObjectName("kamera_x")
        self.kamera_x.textChanged.connect(self.on_xyz_changed)
       
        self.layout_pozycja_kamery.addWidget(self.kamera_x)

        self.kamera_y = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.kamera_y.setObjectName("kamera_y")
        self.kamera_y.textChanged.connect(self.on_xyz_changed)
        
        self.layout_pozycja_kamery.addWidget(self.kamera_y)
        
        self.kamera_z = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.kamera_z.setObjectName("kamera_z")
        self.kamera_z.textChanged.connect(self.on_xyz_changed)
        
        self.layout_pozycja_kamery.addWidget(self.kamera_z)

        

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 150, 171, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layout_kierunek_patrzenia = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layout_kierunek_patrzenia.setContentsMargins(0, 0, 0, 0)
        self.layout_kierunek_patrzenia.setObjectName("layout_kierunek_patrzenia")

        self.patrzenie_x = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.patrzenie_x.setObjectName("patrzenie_x")
       
        self.layout_kierunek_patrzenia.addWidget(self.patrzenie_x)
        self.patrzenie_x.textChanged.connect(self.on_rotate_changed)

        self.patrzenie_y = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.patrzenie_y.setObjectName("patrzenie_y")
        
        self.layout_kierunek_patrzenia.addWidget(self.patrzenie_y)
        self.patrzenie_y.textChanged.connect(self.on_rotate_changed)

        self.patrzenie_z = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.patrzenie_z.setObjectName("patrzenie_z")
    
        self.layout_kierunek_patrzenia.addWidget(self.patrzenie_z)
        self.patrzenie_z.textChanged.connect(self.on_rotate_changed)

        self.label_kierunek_patrzenia = QtWidgets.QLabel(self.centralwidget)
        self.label_kierunek_patrzenia.setGeometry(QtCore.QRect(30, 120, 131, 17))
        self.label_kierunek_patrzenia.setObjectName("label_kierunek_patrzenia")

        self.eliminacja_powierzchni_CB = QtWidgets.QCheckBox(self.centralwidget)
        self.eliminacja_powierzchni_CB.setGeometry(QtCore.QRect(10, 200, 181, 41))
        self.eliminacja_powierzchni_CB.setObjectName("eliminacja_powierzchni_CB")
        #widget w którym rysujemy model
        self.widget_modelu = Widget_rysowania(self.centralwidget)
        self.widget_modelu.setGeometry(QtCore.QRect(259, 19, 431, 361))
        self.widget_modelu.setAutoFillBackground(False)
        self.widget_modelu.setObjectName("widget_modelu")

        self.widget_modelu.set_fields(self.kamera_x, self.kamera_y, self.kamera_z, self.patrzenie_x, self.patrzenie_y, self.patrzenie_z)
        self.eliminacja_powierzchni_CB.stateChanged.connect(self.button_powierzchnia)


        #slider obrotu
        self.rotate_slider = QtWidgets.QSlider(self.centralwidget)
        self.rotate_slider.setGeometry(QtCore.QRect(260, 420, 161, 31))
        self.rotate_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rotate_slider.setObjectName("rotate_slider")
        self.rotate_slider.setMinimum(0)
        self.rotate_slider.setMaximum(360)
        self.rotate_slider.valueChanged.connect(self.on_rotate_slide)

        self.label_rotate = QtWidgets.QLabel(self.centralwidget)
        self.label_rotate.setGeometry(QtCore.QRect(320, 400, 67, 17))
        self.label_rotate.setObjectName("label_rotate")

        self.button_wczytaj_obiekt = QtWidgets.QPushButton(self.centralwidget)
        self.button_wczytaj_obiekt.setGeometry(QtCore.QRect(550, 420, 111, 25))
        self.button_wczytaj_obiekt.setObjectName("button_wczytaj_obiekt")
        self.button_wczytaj_obiekt.clicked.connect(self.klikniecie)


        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.patrzenie_z.setText("0")
        self.patrzenie_y.setText("0")
        self.patrzenie_x.setText("0")
        
        self.kamera_z.setText("0")
        self.kamera_y.setText("0")
        self.kamera_x.setText("0")
        self.show()

    def on_rotate_changed(self):
        if self.patrzenie_x.text() == '' or self.patrzenie_x.text() == '-':
            patrzenie_x = 0
        else:
            patrzenie_x = int(self.patrzenie_x.text())

        if self.patrzenie_y.text() == '' or self.patrzenie_y.text() == '-':
            patrzenie_y = 0
        else:
            patrzenie_y = int(self.patrzenie_y.text())

        if self.patrzenie_z.text() == '' or self.patrzenie_z.text() == '-':
            patrzenie_z = 0
        else:
            patrzenie_z = int(self.patrzenie_z.text())

        self.widget_modelu.obroc(patrzenie_x, patrzenie_y, patrzenie_z)
        self.widget_modelu.update()

    def on_rotate_slide(self):
        obrot = self.rotate_slider.value()
        self.patrzenie_z.setText(str(obrot))

    def on_xyz_changed(self):
        if self.kamera_x.text() == '' or self.kamera_x.text() == "-":
            kamera_x = 0
        else:
            kamera_x = int(self.kamera_x.text())

        if self.kamera_y.text() == '' or self.kamera_y.text() == '-':
            kamera_y = 0
        else:
            kamera_y = int(self.kamera_y.text())

        if self.kamera_z.text() == '' or self.kamera_z.text() == '-':
            kamera_z = 0
        else:
            kamera_z = int(self.kamera_z.text())

        self.widget_modelu.przesun(kamera_x, kamera_y, kamera_z)
        self.widget_modelu.update()

    def klikniecie(self):
        otworz_plik = QFileDialog.getOpenFileName(self, 'Open file','' ,"Object files (*.obj)")
        self.widget_modelu.wstaw_obiekt(file_loader(otworz_plik[0]))
        self.widget_modelu.update()

    def button_powierzchnia(self):
        self.widget_modelu.rysuj_powierzchnie = self.eliminacja_powierzchni_CB.isChecked()
        self.widget_modelu.update()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Prezentacja Modelu 3D"))
        self.label_pozycja_kamery.setText(_translate("MainWindow", "Przesunięcie"))
        self.label_kierunek_patrzenia.setText(_translate("MainWindow", "Obrót"))
        self.eliminacja_powierzchni_CB.setText(_translate("MainWindow", "Eliminacja Powierzchni \n"
"zasłoniętych"))
        self.label_rotate.setText(_translate("MainWindow", "rotate"))
        self.button_wczytaj_obiekt.setText(_translate("MainWindow", "Wczytaj Obiekt"))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Ui_MainWindow()
    okno.setupUi()
    okno.widget_modelu.wstaw_obiekt(file_loader("low-poly-fox-by-pixelmannen.obj"))
    okno.widget_modelu.przesun(0,0,0)
    okno.widget_modelu.obroc(0, 0, 0)
    sys.exit(app.exec_())