
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(653, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainScreen.sizePolicy().hasHeightForWidth())
        MainScreen.setSizePolicy(sizePolicy)
        MainScreen.setMinimumSize(QtCore.QSize(653, 500))
        MainScreen.setMaximumSize(QtCore.QSize(653, 500))
        MainScreen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(35, 37, 38, 255), stop:1 rgba(65, 67, 69, 255));\n"
"color:rgb(170,0,0)")
        self.centralWidget = QtWidgets.QWidget(MainScreen)
        self.centralWidget.setObjectName("centralWidget")
        self.Header_Label = QtWidgets.QLabel(self.centralWidget)
        self.Header_Label.setGeometry(QtCore.QRect(180, 30, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Header_Label.setFont(font)
        self.Header_Label.setStyleSheet("QLabel\n"
"{\n"
"\n"
"background:\n"
"    rgb(0,0,0,0);\n"
"\n"
"color:\n"
"    rgb(170, 0, 0)\n"
"\n"
"}")
        self.Header_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Header_Label.setObjectName("Header_Label")
        self.Start_Button = QtWidgets.QPushButton(self.centralWidget)
        self.Start_Button.setGeometry(QtCore.QRect(220, 170, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Start_Button.setFont(font)
        self.Start_Button.setStyleSheet("QPushButton\n"
"{\n"
"    \n"
"background:\n"
"        qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(237, 0, 0, 69), stop:0.386364 rgba(255, 71, 71, 130), stop:0.423533 rgba(255, 0, 0, 145), stop:0.45 rgba(255, 0, 0, 208), stop:0.477581 rgba(255, 71, 71, 130), stop:0.488636 rgba(255, 1, 1, 69), stop:0.55 rgba(255, 0, 0, 255), stop:0.57754 rgba(255, 0, 0, 130), stop:0.625 rgba(255, 0, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"    \n"
" border: 1px solid black; border-radius: 30px;\n"
"\n"
"color:\n"
"        rgb(255, 255, 255,120);\n"
"\n"
"}    ")
        self.Start_Button.setObjectName("Start_Button")
        self.Quit_Button = QtWidgets.QPushButton(self.centralWidget)
        self.Quit_Button.setGeometry(QtCore.QRect(220, 350, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Quit_Button.setFont(font)
        self.Quit_Button.setStyleSheet("QPushButton\n"
"{\n"
"    \n"
"background:\n"
"        qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(237, 0, 0, 69), stop:0.386364 rgba(255, 71, 71, 130), stop:0.423533 rgba(255, 0, 0, 145), stop:0.45 rgba(255, 0, 0, 208), stop:0.477581 rgba(255, 71, 71, 130), stop:0.488636 rgba(255, 1, 1, 69), stop:0.55 rgba(255, 0, 0, 255), stop:0.57754 rgba(255, 0, 0, 130), stop:0.625 rgba(255, 0, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"    \n"
" border: 1px solid black; border-radius: 30px;\n"
"\n"
"color:\n"
"        rgb(255, 255, 255,120);\n"
"}    ")
        self.Quit_Button.setObjectName("Quit_Button")
        self.background = QtWidgets.QLabel(self.centralWidget)
        self.background.setGeometry(QtCore.QRect(0, -10, 651, 511))
        self.background.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color:rgb(170,0,0)")
        self.background.setText("")
        self.background.setAlignment(QtCore.Qt.AlignCenter)
        self.background.setObjectName("background")
        self.About = QtWidgets.QPushButton(self.centralWidget)
        self.About.setGeometry(QtCore.QRect(220, 260, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.About.setFont(font)
        self.About.setStyleSheet("QPushButton\n"
"{\n"
"    \n"
"background:\n"
"        qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(237, 0, 0, 69), stop:0.386364 rgba(255, 71, 71, 130), stop:0.423533 rgba(255, 0, 0, 145), stop:0.45 rgba(255, 0, 0, 208), stop:0.477581 rgba(255, 71, 71, 130), stop:0.488636 rgba(255, 1, 1, 69), stop:0.55 rgba(255, 0, 0, 255), stop:0.57754 rgba(255, 0, 0, 130), stop:0.625 rgba(255, 0, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"    \n"
" border: 1px solid black; border-radius: 30px;\n"
"\n"
"color:\n"
"        rgb(255, 255, 255,120);\n"
"\n"
"}    ")
        self.About.setObjectName("About")
        self.background.raise_()
        self.Header_Label.raise_()
        self.Start_Button.raise_()
        self.Quit_Button.raise_()
        self.About.raise_()
        MainScreen.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "SudokuSolver"))
        self.Header_Label.setText(_translate("MainScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Sudoku Solver </span></p></body></html>"))
        self.Start_Button.setText(_translate("MainScreen", "Start "))
        self.Quit_Button.setText(_translate("MainScreen", "Quit"))
        self.About.setText(_translate("MainScreen", "About"))

app = QtWidgets.QApplication(sys.argv)
mainscreen = QtWidgets.QMainWindow()
ui_main = Ui_MainScreen()
ui_main.setupUi(mainscreen)


