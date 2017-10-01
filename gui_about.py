
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        About.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(35, 37, 38, 255), stop:1 rgba(65, 67, 69, 255));\n"
"color:rgb(170,0,0)")
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        About.setCentralWidget(self.centralwidget)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "MainWindow"))



About = QtWidgets.QMainWindow()
ui = Ui_About()
ui.setupUi(About)
    

