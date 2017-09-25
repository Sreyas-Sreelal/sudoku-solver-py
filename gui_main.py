

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sudoku_main(object):
    def setupUi(self, sudoku_main):
        sudoku_main.setObjectName("sudoku_main")
        sudoku_main.resize(734, 603)
        sudoku_main.setStyleSheet("QWidget\n"
"{\n"
"\n"
"background:\n"
"    rgb(0, 0, 0);\n"
"}")
        self.box4 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box4.setGeometry(QtCore.QRect(290, 90, 30, 30))
        self.box4.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box4.setPlainText("")
        self.box4.setObjectName("box4")
        self.box5 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box5.setGeometry(QtCore.QRect(340, 90, 30, 30))
        self.box5.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box5.setPlainText("")
        self.box5.setObjectName("box5")
        self.box6 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box6.setGeometry(QtCore.QRect(390, 90, 30, 30))
        self.box6.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box6.setPlainText("")
        self.box6.setObjectName("box6")
        self.box13 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box13.setGeometry(QtCore.QRect(290, 130, 30, 30))
        self.box13.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box13.setPlainText("")
        self.box13.setObjectName("box13")
        self.box14 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box14.setGeometry(QtCore.QRect(340, 130, 30, 30))
        self.box14.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box14.setPlainText("")
        self.box14.setObjectName("box14")
        self.box15 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box15.setGeometry(QtCore.QRect(390, 130, 30, 30))
        self.box15.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box15.setPlainText("")
        self.box15.setObjectName("box15")
        self.box22 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box22.setGeometry(QtCore.QRect(290, 170, 30, 30))
        self.box22.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box22.setPlainText("")
        self.box22.setObjectName("box22")
        self.box23 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box23.setGeometry(QtCore.QRect(340, 170, 30, 30))
        self.box23.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box23.setPlainText("")
        self.box23.setObjectName("box23")
        self.box24 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box24.setGeometry(QtCore.QRect(390, 170, 30, 30))
        self.box24.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box24.setPlainText("")
        self.box24.setObjectName("box24")
        self.box40 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box40.setGeometry(QtCore.QRect(290, 281, 30, 30))
        self.box40.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box40.setPlainText("")
        self.box40.setObjectName("box40")
        self.box31 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box31.setGeometry(QtCore.QRect(290, 241, 30, 30))
        self.box31.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box31.setPlainText("")
        self.box31.setObjectName("box31")
        self.box49 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box49.setGeometry(QtCore.QRect(290, 321, 30, 30))
        self.box49.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box49.setPlainText("")
        self.box49.setObjectName("box49")
        self.box67 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box67.setGeometry(QtCore.QRect(290, 429, 30, 30))
        self.box67.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box67.setPlainText("")
        self.box67.setObjectName("box67")
        self.box58 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box58.setGeometry(QtCore.QRect(290, 389, 30, 30))
        self.box58.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box58.setPlainText("")
        self.box58.setObjectName("box58")
        self.box76 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box76.setGeometry(QtCore.QRect(290, 469, 30, 30))
        self.box76.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box76.setPlainText("")
        self.box76.setObjectName("box76")
        self.box50 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box50.setGeometry(QtCore.QRect(340, 320, 30, 30))
        self.box50.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box50.setPlainText("")
        self.box50.setObjectName("box50")
        self.box41 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box41.setGeometry(QtCore.QRect(340, 280, 30, 30))
        self.box41.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box41.setPlainText("")
        self.box41.setObjectName("box41")
        self.box32 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box32.setGeometry(QtCore.QRect(340, 240, 30, 30))
        self.box32.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box32.setPlainText("")
        self.box32.setObjectName("box32")
        self.box59 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box59.setGeometry(QtCore.QRect(340, 390, 30, 30))
        self.box59.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box59.setPlainText("")
        self.box59.setObjectName("box59")
        self.box68 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box68.setGeometry(QtCore.QRect(340, 430, 30, 30))
        self.box68.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box68.setPlainText("")
        self.box68.setObjectName("box68")
        self.box77 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box77.setGeometry(QtCore.QRect(340, 470, 30, 30))
        self.box77.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box77.setPlainText("")
        self.box77.setObjectName("box77")
        self.box33 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box33.setGeometry(QtCore.QRect(390, 240, 30, 30))
        self.box33.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box33.setPlainText("")
        self.box33.setObjectName("box33")
        self.box42 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box42.setGeometry(QtCore.QRect(390, 280, 30, 30))
        self.box42.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box42.setPlainText("")
        self.box42.setObjectName("box42")
        self.box51 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box51.setGeometry(QtCore.QRect(390, 320, 30, 30))
        self.box51.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box51.setPlainText("")
        self.box51.setObjectName("box51")
        self.box60 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box60.setGeometry(QtCore.QRect(390, 390, 30, 30))
        self.box60.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box60.setPlainText("")
        self.box60.setObjectName("box60")
        self.box69 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box69.setGeometry(QtCore.QRect(390, 430, 30, 30))
        self.box69.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box69.setPlainText("")
        self.box69.setObjectName("box69")
        self.box78 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box78.setGeometry(QtCore.QRect(390, 470, 30, 30))
        self.box78.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box78.setPlainText("")
        self.box78.setObjectName("box78")
        self.box3 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box3.setGeometry(QtCore.QRect(220, 90, 30, 30))
        self.box3.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box3.setPlainText("")
        self.box3.setObjectName("box3")
        self.box12 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box12.setGeometry(QtCore.QRect(220, 130, 30, 30))
        self.box12.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box12.setPlainText("")
        self.box12.setObjectName("box12")
        self.box21 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box21.setGeometry(QtCore.QRect(220, 170, 30, 30))
        self.box21.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box21.setPlainText("")
        self.box21.setObjectName("box21")
        self.box30 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box30.setGeometry(QtCore.QRect(220, 240, 30, 30))
        self.box30.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box30.setPlainText("")
        self.box30.setObjectName("box30")
        self.box39 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box39.setGeometry(QtCore.QRect(220, 280, 30, 30))
        self.box39.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box39.setPlainText("")
        self.box39.setObjectName("box39")
        self.box48 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box48.setGeometry(QtCore.QRect(220, 320, 30, 30))
        self.box48.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box48.setPlainText("")
        self.box48.setObjectName("box48")
        self.box57 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box57.setGeometry(QtCore.QRect(220, 390, 30, 30))
        self.box57.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box57.setPlainText("")
        self.box57.setObjectName("box57")
        self.box66 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box66.setGeometry(QtCore.QRect(220, 430, 30, 30))
        self.box66.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box66.setPlainText("")
        self.box66.setObjectName("box66")
        self.box75 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box75.setGeometry(QtCore.QRect(220, 470, 30, 30))
        self.box75.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box75.setPlainText("")
        self.box75.setObjectName("box75")
        self.box2 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box2.setGeometry(QtCore.QRect(170, 90, 30, 30))
        self.box2.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box2.setPlainText("")
        self.box2.setObjectName("box2")
        self.box11 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box11.setGeometry(QtCore.QRect(170, 130, 30, 30))
        self.box11.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box11.setPlainText("")
        self.box11.setObjectName("box11")
        self.box20 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box20.setGeometry(QtCore.QRect(170, 170, 30, 30))
        self.box20.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box20.setPlainText("")
        self.box20.setObjectName("box20")
        self.box1 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box1.setGeometry(QtCore.QRect(120, 90, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.box1.setFont(font)
        self.box1.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box1.setPlainText("")
        self.box1.setObjectName("box1")
        self.box10 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box10.setGeometry(QtCore.QRect(120, 130, 30, 30))
        self.box10.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box10.setPlainText("")
        self.box10.setObjectName("box10")
        self.box19 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box19.setGeometry(QtCore.QRect(120, 170, 30, 30))
        self.box19.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box19.setPlainText("")
        self.box19.setObjectName("box19")
        self.box29 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box29.setGeometry(QtCore.QRect(170, 240, 30, 30))
        self.box29.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box29.setPlainText("")
        self.box29.setObjectName("box29")
        self.box38 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box38.setGeometry(QtCore.QRect(170, 280, 30, 30))
        self.box38.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box38.setPlainText("")
        self.box38.setObjectName("box38")
        self.box47 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box47.setGeometry(QtCore.QRect(170, 320, 30, 30))
        self.box47.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box47.setPlainText("")
        self.box47.setObjectName("box47")
        self.box28 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box28.setGeometry(QtCore.QRect(120, 240, 30, 30))
        self.box28.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box28.setPlainText("")
        self.box28.setObjectName("box28")
        self.box37 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box37.setGeometry(QtCore.QRect(120, 280, 30, 30))
        self.box37.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box37.setPlainText("")
        self.box37.setObjectName("box37")
        self.box46 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box46.setGeometry(QtCore.QRect(120, 320, 30, 30))
        self.box46.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box46.setPlainText("")
        self.box46.setObjectName("box46")
        self.box56 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box56.setGeometry(QtCore.QRect(170, 390, 30, 30))
        self.box56.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box56.setPlainText("")
        self.box56.setObjectName("box56")
        self.box65 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box65.setGeometry(QtCore.QRect(170, 430, 30, 30))
        self.box65.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box65.setPlainText("")
        self.box65.setObjectName("box65")
        self.box74 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box74.setGeometry(QtCore.QRect(170, 470, 30, 30))
        self.box74.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box74.setPlainText("")
        self.box74.setObjectName("box74")
        self.box55 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box55.setGeometry(QtCore.QRect(120, 390, 30, 30))
        self.box55.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box55.setPlainText("")
        self.box55.setObjectName("box55")
        self.box64 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box64.setGeometry(QtCore.QRect(120, 430, 30, 30))
        self.box64.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box64.setPlainText("")
        self.box64.setObjectName("box64")
        self.box73 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box73.setGeometry(QtCore.QRect(120, 470, 30, 30))
        self.box73.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box73.setPlainText("")
        self.box73.setObjectName("box73")
        self.box7 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box7.setGeometry(QtCore.QRect(460, 90, 30, 30))
        self.box7.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box7.setPlainText("")
        self.box7.setObjectName("box7")
        self.box16 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box16.setGeometry(QtCore.QRect(460, 130, 30, 30))
        self.box16.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box16.setPlainText("")
        self.box16.setObjectName("box16")
        self.box25 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box25.setGeometry(QtCore.QRect(460, 170, 30, 30))
        self.box25.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box25.setPlainText("")
        self.box25.setObjectName("box25")
        self.box34 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box34.setGeometry(QtCore.QRect(460, 240, 30, 30))
        self.box34.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box34.setPlainText("")
        self.box34.setObjectName("box34")
        self.box43 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box43.setGeometry(QtCore.QRect(460, 280, 30, 30))
        self.box43.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box43.setPlainText("")
        self.box43.setObjectName("box43")
        self.box52 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box52.setGeometry(QtCore.QRect(460, 320, 30, 30))
        self.box52.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box52.setPlainText("")
        self.box52.setObjectName("box52")
        self.box61 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box61.setGeometry(QtCore.QRect(460, 390, 30, 30))
        self.box61.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box61.setPlainText("")
        self.box61.setObjectName("box61")
        self.box70 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box70.setGeometry(QtCore.QRect(460, 430, 30, 30))
        self.box70.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box70.setPlainText("")
        self.box70.setObjectName("box70")
        self.box79 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box79.setGeometry(QtCore.QRect(460, 470, 30, 30))
        self.box79.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box79.setPlainText("")
        self.box79.setObjectName("box79")
        self.box8 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box8.setGeometry(QtCore.QRect(510, 90, 30, 30))
        self.box8.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box8.setPlainText("")
        self.box8.setObjectName("box8")
        self.box17 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box17.setGeometry(QtCore.QRect(510, 130, 30, 30))
        self.box17.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box17.setPlainText("")
        self.box17.setObjectName("box17")
        self.box26 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box26.setGeometry(QtCore.QRect(510, 170, 30, 30))
        self.box26.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box26.setPlainText("")
        self.box26.setObjectName("box26")
        self.box35 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box35.setGeometry(QtCore.QRect(510, 240, 30, 30))
        self.box35.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box35.setPlainText("")
        self.box35.setObjectName("box35")
        self.box44 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box44.setGeometry(QtCore.QRect(510, 280, 30, 30))
        self.box44.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box44.setPlainText("")
        self.box44.setObjectName("box44")
        self.box53 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box53.setGeometry(QtCore.QRect(510, 320, 30, 30))
        self.box53.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box53.setPlainText("")
        self.box53.setObjectName("box53")
        self.box62 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box62.setGeometry(QtCore.QRect(510, 390, 30, 30))
        self.box62.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box62.setPlainText("")
        self.box62.setObjectName("box62")
        self.box71 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box71.setGeometry(QtCore.QRect(510, 430, 30, 30))
        self.box71.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box71.setPlainText("")
        self.box71.setObjectName("box71")
        self.box80 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box80.setGeometry(QtCore.QRect(510, 470, 30, 30))
        self.box80.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box80.setPlainText("")
        self.box80.setObjectName("box80")
        self.box63 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box63.setGeometry(QtCore.QRect(560, 390, 30, 30))
        self.box63.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box63.setPlainText("")
        self.box63.setObjectName("box63")
        self.box72 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box72.setGeometry(QtCore.QRect(560, 430, 30, 30))
        self.box72.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box72.setPlainText("")
        self.box72.setObjectName("box72")
        self.box81 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box81.setGeometry(QtCore.QRect(560, 470, 30, 30))
        self.box81.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box81.setPlainText("")
        self.box81.setObjectName("box81")
        self.box36 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box36.setGeometry(QtCore.QRect(560, 240, 30, 30))
        self.box36.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box36.setPlainText("")
        self.box36.setObjectName("box36")
        self.box45 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box45.setGeometry(QtCore.QRect(560, 280, 30, 30))
        self.box45.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box45.setPlainText("")
        self.box45.setObjectName("box45")
        self.box54 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box54.setGeometry(QtCore.QRect(560, 320, 30, 30))
        self.box54.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box54.setPlainText("")
        self.box54.setObjectName("box54")
        self.box9 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box9.setGeometry(QtCore.QRect(560, 90, 30, 30))
        self.box9.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box9.setPlainText("")
        self.box9.setObjectName("box9")
        self.box18 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box18.setGeometry(QtCore.QRect(560, 130, 30, 30))
        self.box18.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box18.setPlainText("")
        self.box18.setObjectName("box18")
        self.box27 = QtWidgets.QPlainTextEdit(sudoku_main)
        self.box27.setGeometry(QtCore.QRect(560, 170, 30, 30))
        self.box27.setStyleSheet("QPlainTextEdit\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.box27.setPlainText("")
        self.box27.setObjectName("box27")
        self.label = QtWidgets.QLabel(sudoku_main)
        self.label.setGeometry(QtCore.QRect(120, 30, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"background:\n"
"rgb(0,0,0,0);\n"
"color:\n"
"rgb(255,0,120,230);\n"
"}")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(sudoku_main)
        self.pushButton.setGeometry(QtCore.QRect(110, 530, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"border:1px solid black;\n"
"border-radius:10px;\n"
"background:\n"
"qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(237, 0, 0, 69), stop:0.386364 rgba(255, 71, 71, 130), stop:0.423533 rgba(255, 0, 0, 145), stop:0.45 rgba(255, 0, 0, 208), stop:0.477581 rgba(255, 71, 71, 130), stop:0.488636 rgba(255, 1, 1, 69), stop:0.55 rgba(255, 0, 0, 255), stop:0.57754 rgba(255, 0, 0, 130), stop:0.625 rgba(255, 0, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"color:\n"
"rgb(255,255,255,120);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.background = QtWidgets.QLabel(sudoku_main)
        self.background.setGeometry(QtCore.QRect(170, 120, 361, 301))
        self.background.setStyleSheet("")
        self.background.setText("")
        self.background.setAlignment(QtCore.Qt.AlignCenter)
        self.background.setObjectName("background")
        self.background.raise_()
        self.box4.raise_()
        self.box5.raise_()
        self.box6.raise_()
        self.box13.raise_()
        self.box14.raise_()
        self.box15.raise_()
        self.box22.raise_()
        self.box23.raise_()
        self.box24.raise_()
        self.box40.raise_()
        self.box31.raise_()
        self.box49.raise_()
        self.box67.raise_()
        self.box58.raise_()
        self.box76.raise_()
        self.box50.raise_()
        self.box41.raise_()
        self.box32.raise_()
        self.box59.raise_()
        self.box68.raise_()
        self.box77.raise_()
        self.box33.raise_()
        self.box42.raise_()
        self.box51.raise_()
        self.box60.raise_()
        self.box69.raise_()
        self.box78.raise_()
        self.box3.raise_()
        self.box12.raise_()
        self.box21.raise_()
        self.box30.raise_()
        self.box39.raise_()
        self.box48.raise_()
        self.box57.raise_()
        self.box66.raise_()
        self.box75.raise_()
        self.box2.raise_()
        self.box11.raise_()
        self.box20.raise_()
        self.box1.raise_()
        self.box10.raise_()
        self.box19.raise_()
        self.box29.raise_()
        self.box38.raise_()
        self.box47.raise_()
        self.box28.raise_()
        self.box37.raise_()
        self.box46.raise_()
        self.box56.raise_()
        self.box65.raise_()
        self.box74.raise_()
        self.box55.raise_()
        self.box64.raise_()
        self.box73.raise_()
        self.box7.raise_()
        self.box16.raise_()
        self.box25.raise_()
        self.box34.raise_()
        self.box43.raise_()
        self.box52.raise_()
        self.box61.raise_()
        self.box70.raise_()
        self.box79.raise_()
        self.box8.raise_()
        self.box17.raise_()
        self.box26.raise_()
        self.box35.raise_()
        self.box44.raise_()
        self.box53.raise_()
        self.box62.raise_()
        self.box71.raise_()
        self.box80.raise_()
        self.box63.raise_()
        self.box72.raise_()
        self.box81.raise_()
        self.box36.raise_()
        self.box45.raise_()
        self.box54.raise_()
        self.box9.raise_()
        self.box18.raise_()
        self.box27.raise_()
        self.label.raise_()
        self.pushButton.raise_()

        self.retranslateUi(sudoku_main)
        QtCore.QMetaObject.connectSlotsByName(sudoku_main)

    def retranslateUi(self, sudoku_main):
        _translate = QtCore.QCoreApplication.translate
        sudoku_main.setWindowTitle(_translate("sudoku_main", "SudokuSolver"))
        self.label.setText(_translate("sudoku_main", "Insert the numbers in corresponding column. Leave empty columns as it is."))
        self.pushButton.setText(_translate("sudoku_main", "Solve Sudoku Puzzle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sudoku_main = QtWidgets.QWidget()
    ui = Ui_sudoku_main()
    ui.setupUi(sudoku_main)
    sudoku_main.show()
    sys.exit(app.exec_())

