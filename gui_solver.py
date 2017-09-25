
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SudokuSolver(object):
    def setupUi(self, SudokuSolver):
        SudokuSolver.setObjectName("SudokuSolver")
        SudokuSolver.resize(653, 500)
        SudokuSolver.setStyleSheet("QWidget\n"
"{\n"
"\n"
"background:\n"
"    rgb(0, 0, 0)\n"
"\n"
"}")
        self.centralWidget = QtWidgets.QWidget(SudokuSolver)
        self.centralWidget.setObjectName("centralWidget")
        self.Header_Label = QtWidgets.QLabel(self.centralWidget)
        self.Header_Label.setGeometry(QtCore.QRect(170, 30, 281, 71))
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
        self.Start_Button.setGeometry(QtCore.QRect(210, 200, 201, 61))
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
        self.Quit_Button.setGeometry(QtCore.QRect(210, 330, 201, 61))
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
        self.background.setGeometry(QtCore.QRect(50, 0, 561, 301))
        self.background.setStyleSheet("")
        self.background.setText("")
        self.background.setAlignment(QtCore.Qt.AlignCenter)
        self.background.setObjectName("background")
        self.credits = QtWidgets.QLabel(self.centralWidget)
        self.credits.setGeometry(QtCore.QRect(430, 410, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.credits.setFont(font)
        self.credits.setStyleSheet("QLabel\n"
"{\n"
"\n"
"background:\n"
"    rgb(0,0,0,0);\n"
"\n"
"color:\n"
"    rgb(255, 255, 123,123)\n"
"\n"
"}")
        self.credits.setAlignment(QtCore.Qt.AlignCenter)
        self.credits.setObjectName("credits")
        self.background.raise_()
        self.Header_Label.raise_()
        self.Start_Button.raise_()
        self.Quit_Button.raise_()
        self.credits.raise_()
        SudokuSolver.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(SudokuSolver)
        self.statusBar.setObjectName("statusBar")
        SudokuSolver.setStatusBar(self.statusBar)

        self.retranslateUi(SudokuSolver)
        QtCore.QMetaObject.connectSlotsByName(SudokuSolver)

    def retranslateUi(self, SudokuSolver):
        _translate = QtCore.QCoreApplication.translate
        SudokuSolver.setWindowTitle(_translate("SudokuSolver", "SudokuSolver"))
        self.Header_Label.setText(_translate("SudokuSolver", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Sudoku Solver </span></p></body></html>"))
        self.Start_Button.setText(_translate("SudokuSolver", "Start "))
        self.Quit_Button.setText(_translate("SudokuSolver", "Quit"))
        self.credits.setText(_translate("SudokuSolver", "Created by Sreyas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SudokuSolver = QtWidgets.QMainWindow()
    ui = Ui_SudokuSolver()
    ui.setupUi(SudokuSolver)
    SudokuSolver.show()
    sys.exit(app.exec_())

