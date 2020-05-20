# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
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
        self.kamera_x = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.kamera_x.setObjectName("kamera_x")
        self.layout_pozycja_kamery.addWidget(self.kamera_x)
        self.kamera_y = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.kamera_y.setObjectName("kamera_y")
        self.layout_pozycja_kamery.addWidget(self.kamera_y)
        self.kamera_z = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.kamera_z.setObjectName("kamera_z")
        self.layout_pozycja_kamery.addWidget(self.kamera_z)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 150, 171, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layout_kierunek_patrzenia = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layout_kierunek_patrzenia.setContentsMargins(0, 0, 0, 0)
        self.layout_kierunek_patrzenia.setObjectName("layout_kierunek_patrzenia")
        self.patrzenie_x = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.patrzenie_x.setObjectName("patrzenie_x")
        self.layout_kierunek_patrzenia.addWidget(self.patrzenie_x)
        self.patrzenie_y = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.patrzenie_y.setObjectName("patrzenie_y")
        self.layout_kierunek_patrzenia.addWidget(self.patrzenie_y)
        self.patrzenie_z = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.patrzenie_z.setObjectName("patrzenie_z")
        self.layout_kierunek_patrzenia.addWidget(self.patrzenie_z)
        self.label_kierunek_patrzenia = QtWidgets.QLabel(self.centralwidget)
        self.label_kierunek_patrzenia.setGeometry(QtCore.QRect(30, 120, 131, 17))
        self.label_kierunek_patrzenia.setObjectName("label_kierunek_patrzenia")
        self.eliminacja_powierzchni_CB = QtWidgets.QCheckBox(self.centralwidget)
        self.eliminacja_powierzchni_CB.setGeometry(QtCore.QRect(10, 200, 181, 41))
        self.eliminacja_powierzchni_CB.setObjectName("eliminacja_powierzchni_CB")
        self.oswietlenie_CB = QtWidgets.QCheckBox(self.centralwidget)
        self.oswietlenie_CB.setGeometry(QtCore.QRect(10, 270, 101, 23))
        self.oswietlenie_CB.setObjectName("oswietlenie_CB")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 310, 171, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.layout_oswietlenie = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.layout_oswietlenie.setContentsMargins(0, 0, 0, 0)
        self.layout_oswietlenie.setObjectName("layout_oswietlenie")
        self.swiatlo_x = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.swiatlo_x.setObjectName("swiatlo_x")
        self.layout_oswietlenie.addWidget(self.swiatlo_x)
        self.swiatlo_y = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.swiatlo_y.setObjectName("swiatlo_y")
        self.layout_oswietlenie.addWidget(self.swiatlo_y)
        self.swiatlo_z = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.swiatlo_z.setObjectName("swiatlo_z")
        self.layout_oswietlenie.addWidget(self.swiatlo_z)

        self.widget_modelu = Widget_rysowania(self.centralwidget)
        self.widget_modelu.setGeometry(QtCore.QRect(259, 19, 431, 361))
        self.widget_modelu.setAutoFillBackground(False)
        self.widget_modelu.setObjectName("widget_modelu")

        self.zoom_slider = QtWidgets.QSlider(self.centralwidget)
        self.zoom_slider.setGeometry(QtCore.QRect(260, 420, 161, 31))
        self.zoom_slider.setOrientation(QtCore.Qt.Horizontal)
        self.zoom_slider.setObjectName("zoom_slider")
        self.label_zoom = QtWidgets.QLabel(self.centralwidget)
        self.label_zoom.setGeometry(QtCore.QRect(320, 400, 67, 17))
        self.label_zoom.setObjectName("label_zoom")
        self.button_wczytaj_obiekt = QtWidgets.QPushButton(self.centralwidget)
        self.button_wczytaj_obiekt.setGeometry(QtCore.QRect(550, 420, 111, 25))
        self.button_wczytaj_obiekt.setObjectName("button_wczytaj_obiekt")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Prezentacja Modelu 3D"))
        self.label_pozycja_kamery.setText(_translate("MainWindow", "Pozycja Kamery"))
        self.label_kierunek_patrzenia.setText(_translate("MainWindow", "Kierunek Patrzenia"))
        self.eliminacja_powierzchni_CB.setText(_translate("MainWindow", "Eliminacja Powierzchni \n"
"zasłoniętych"))
        self.oswietlenie_CB.setText(_translate("MainWindow", "Oświetlenie"))
        self.label_zoom.setText(_translate("MainWindow", "Zoom"))
        self.button_wczytaj_obiekt.setText(_translate("MainWindow", "Wczytaj Obiekt"))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Ui_MainWindow()
    okno.setupUi()
    okno.widget_modelu.wstaw_obiekt(file_loader())
    okno.widget_modelu.przesun(-150, -150, 0)
    sys.exit(app.exec_())