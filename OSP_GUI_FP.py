## Course: CST 205
## Title: Final Project
## Date: 12/14/20
## Authors: Jason Baker, Joseph Castro, Julian Fortin, Emerson Jimenez
## Github: https://github.com/PHRZNForeign/Team31_CST205
## Abstract: This program opens a visual GUI for the user to fill in location names and it performs operations to show relevant locational data using geopy API
​
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
​
# pip install geopy
import geopy
from geopy.geocoders import Nominatim as nom
from geopy.distance import geodesic 
​
# geopy API key, using a generic name for user-agent gives a 403 forbidden error
geolocator = nom(user_agent="cst205final-project")
​
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # set name and dimensions for out GUI box
        self.setWindowTitle('Geography lookup')
        self.setGeometry(100,100,500,300)
        vbox = QVBoxLayout()
        
        # line edits used for entering in the locations what will talk to the geopy api
        self.my_line = QLineEdit(self)
        self.my_line2 = QLineEdit(self)
        self.my_lbl = QLabel('Enter a location name:')
        self.my_lbl2 = QLabel('')
        self.my_lbl3 = QLabel('Enter second location name (Distance only):')
        
        # combo box will decide what operations are performed on the locations entered into the line edits
        self.my_cb = QComboBox()
        self.my_cb.addItems(["Lat/Long", "Address", "Category", "Type", "Distance"])
        
        # button that will connect to the function and activate the method chosen in combo box
        self.my_btn = QPushButton("GO")
        self.my_btn.move(30,16)
        self.my_btn.clicked.connect(self.btn_go)
        
        # set second line edit to read only unless 'Distance' is chosen in combo box
        self.my_line2.setReadOnly(True)
        self.my_cb.currentIndexChanged.connect(self.ichange)
        
        # arrange the widgets in the right order
        vbox.addWidget(self.my_lbl)
        vbox.addWidget(self.my_line)
        vbox.addWidget(self.my_lbl3)
        vbox.addWidget(self.my_line2)
        vbox.addWidget(self.my_cb)        
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_lbl2)
        self.setLayout(vbox)
    @Slot()
    
    # function that activates on button press
    def btn_go(self):
        # getting line edit string data
        userinput = self.my_line.text()
        userinput2 = self.my_line2.text()
        
        # put line edit data through geopy API geolocator 
        location = geolocator.geocode(userinput, language='en')
        location2 = geolocator.geocode(userinput2, language='en')
        
        # check index of the combo box and format to print
        index = self.my_cb.currentIndex()
        if (index == 0):
            str = "Latitude and Longitude: {}, {}".format(location.latitude, location.longitude)
        elif(index == 1):
            str = "Address: {}".format(location.address)
        elif(index == 2):
            str = "Category: {}".format(location.raw['class'])
        elif(index == 3):
            str = "Type: {}".format(location.raw['type'])
        elif(index == 4):
            str = "Distance (in km): {}".format(geodesic((location.latitude, location.longitude), (location2.latitude, location2.longitude)).km)
        
        # display the chosen information at the bottom of the window
        self.my_lbl2.setText(str)
        self.repaint()
        
    # function to check the combo box index
    def ichange(self):
        index = self.my_cb.currentIndex()
        
        # Only enable second line edit when combo box is set to 'Distance'
        if (index == 4):
            self.my_line2.setReadOnly(False)
        else:
            self.my_line2.setReadOnly(True)
            self.my_line2.setText('')
        
app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()