# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:26:28 2020
​
@author: jabak_000
"""
​
import sys
import geopy
from geopy.geocoders import Nominatim as nom
from PySide2.QtWidgets import *
from PySide2.QtCore import *
​
geolocator = nom(user_agent="cst205final-project")
​
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        self.my_line = QLineEdit(self)
        self.my_btn = QPushButton("Lat. and Long.")
        self.my_btn.move(30,16)
        self.my_lbl = QLabel('Enter a location name')
        self.my_btn.clicked.connect(self.lat_long)
        self.my_btn2 = QPushButton("Address")
        self.my_btn2.move(30,16)
        self.my_btn2.clicked.connect(self.add)
        vbox.addWidget(self.my_line)
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_btn2)
        vbox.addWidget(self.my_lbl)
        self.setLayout(vbox)
    @Slot()
    def lat_long(self):
        userinput = self.my_line.text()
        location = geolocator.geocode(userinput)
        str = "Latitude and Longitude: {}, {}".format(location.latitude, location.longitude)
        self.my_lbl.setText(str)
        self.repaint()
    def add(self):
        userinput = self.my_line.text()
        location = geolocator.geocode(userinput)
        str = "Address: {}".format(location.address)
        self.my_lbl.setText(str)
        self.repaint()
app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()