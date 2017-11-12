from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(653, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        About.setMinimumSize(QtCore.QSize(653, 500))
        About.setMaximumSize(QtCore.QSize(653, 500))
        About.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(35, 37, 38, 255), stop:1 rgba(65, 67, 69, 255));\n"
"color:rgb(170,0,0)")
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(590, 500, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("    \n"
"background:\n"
"        qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(237, 0, 0, 69), stop:0.386364 rgba(255, 71, 71, 130), stop:0.423533 rgba(255, 0, 0, 145), stop:0.45 rgba(255, 0, 0, 208), stop:0.477581 rgba(255, 71, 71, 130), stop:0.488636 rgba(255, 1, 1, 69), stop:0.55 rgba(255, 0, 0, 255), stop:0.57754 rgba(255, 0, 0, 130), stop:0.625 rgba(255, 0, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"    \n"
" border: 1px solid black; \n"
" border-radius: 9px;\n"
"\n"
"color:\n"
"        rgb(255, 255, 255,120);\n"
"\n"
"    ")
        self.back_button.setObjectName("back_button")
        self.team_members_label = QtWidgets.QLabel(self.centralwidget)
        self.team_members_label.setGeometry(QtCore.QRect(40, 80, 571, 341))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.team_members_label.setFont(font)
        self.team_members_label.setStyleSheet("background : none;")
        self.team_members_label.setObjectName("team_members_label")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -1, 653, 500))
        self.background.setMinimumSize(QtCore.QSize(653, 500))
        self.background.setMaximumSize(QtCore.QSize(653, 500))
        self.background.setText("")
        self.background.setObjectName("background")
        self.Back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(11, 420, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Back_Button.setFont(font)
        self.Back_Button.setStyleSheet("QPushButton\n"
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
        self.Back_Button.setObjectName("Back_Button")
        self.background.raise_()
        self.back_button.raise_()
        self.team_members_label.raise_()
        self.Back_Button.raise_()
        About.setCentralWidget(self.centralwidget)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.back_button.setText(_translate("About", "Back"))
        self.team_members_label.setText(_translate("About", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#00ff7f;\">Team Members</span></p><p align=\"center\"><span style=\" font-size:18pt; color:#0000ff;\">Leon</span></p><p align=\"center\"><span style=\" font-size:18pt; color:#0000ff;\">Mridhul</span></p><p align=\"center\"><span style=\" font-size:18pt; color:#0000ff;\">Renuka</span></p><p align=\"center\"><span style=\" font-size:18pt; color:#0000ff;\">Sandra</span></p><p align=\"center\"><span style=\" font-size:18pt; color:#0000ff;\">Sreyas</span></p><p align=\"center\"><br/></p></body></html>"))
        self.Back_Button.setText(_translate("About", "Back"))

about_screen = QtWidgets.QMainWindow()
ui_about = Ui_About()
ui_about.setupUi(about_screen)



