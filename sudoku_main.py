import sys
from gui_main import mainscreen,ui_main,app
from gui_solver import solver_screen,ui_screen
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QMovie

def UAN(a,i,j): 
 
    for i in range(0,9): 
        for j in range(0,9): 
            if a[i][j] == 0: 
                return i,j 
    return -1,-1  

def ROW(a,idx,num): 
 
    for i in range(0,9): 
        if a[idx][i] == num: 
            return True 
    return False
 

def COL(a,idx,num): 
 
    for i in range(0,9):
        if a[i][idx] == num : 
            return True
    return False 
 

def GRID(a,i,j,num): 

    for u in range(0,3):
        for y in range(0,3): 
            if a[i+u][j+y] == num: 
                return True 
    return False
 

def safe(a,i,j,num): 
 
    if not ROW(a,i,num) and not COL(a,j,num) and not GRID(a,i-i%3,j-j%3,num): 
        return True 
    return False 
 

def checkvalidity(a):
    for i in range(0,9):
        for j in range(0,9):
            if a[i][j]  not in range(0,10):
                return False
    return True

def solve(a,i=0,j=0): 

    i,j = UAN(a,i,j)
    if  i == -1: 
         return True 
    for k in range(1,10): 
     
        if safe(a,i,j,k): 
         
            a[i][j] = k  

            if solve(a): 
                return True 
            a[i][j] = 0 
         
     
    return False 
 

"""
Sample matrix for testing 
   
    a = [ 
        [0,8,0, 7,1,2, 0,9,0], 
        [0,0,0, 0,0,0, 7,1,0], 
        [0,0,0, 0,9,4, 2,6,0], 
         
        [0,0,0, 3,6,0, 4,0,5], 
        [5,0,0, 0,0,0, 0,0,9], 
        [7,0,6, 0,2,5, 0,0,0], 
         
        [0,5,8, 2,7,0, 0,0,0], 
        [0,1,7, 0,0,0, 0,0,0], 
        [0,6,0, 9,4,1, 0,5,7] 
    ]
     
"""
def shownextscreen():
    mainscreen.hide()
    bgimg = QMovie("source.gif")
    ui_screen.background.autoFillBackground()
    #ui_screen.background.resize(solver_screen.size())
    ui_screen.background.setMovie(bgimg)
    bgimg.setScaledSize(solver_screen.size())
    bgimg.start()
    solver_screen.show()

def str2int(buffer):
    if buffer == None or buffer == "":
        return 0
    else:
        return int(buffer)
    
def startsolving():
    a = [ 
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0] 
        
    ]
    a[0][0] = str2int (ui_screen.box1.toPlainText())
    a[0][1] = str2int (ui_screen.box2.toPlainText())
    a[0][2] = str2int (ui_screen.box3.toPlainText())
    a[0][3] = str2int (ui_screen.box4.toPlainText())
    a[0][4] = str2int (ui_screen.box5.toPlainText())
    a[0][5] = str2int (ui_screen.box6.toPlainText())
    a[0][6] = str2int (ui_screen.box7.toPlainText())
    a[0][7] = str2int (ui_screen.box8.toPlainText())
    a[0][8] = str2int (ui_screen.box9.toPlainText())

    a[0][0] = str2int (ui_screen.box10.toPlainText())
    a[1][1] = str2int (ui_screen.box11.toPlainText())
    a[1][2] = str2int (ui_screen.box12.toPlainText())
    a[1][3] = str2int (ui_screen.box13.toPlainText())
    a[1][4] = str2int (ui_screen.box14.toPlainText())
    a[1][5] = str2int (ui_screen.box15.toPlainText())
    a[1][6] = str2int (ui_screen.box16.toPlainText())
    a[1][7] = str2int (ui_screen.box17.toPlainText())
    a[1][8] = str2int (ui_screen.box18.toPlainText())

    a[2][0] = str2int (ui_screen.box19.toPlainText())
    a[2][1] = str2int (ui_screen.box20.toPlainText())
    a[2][2] = str2int (ui_screen.box21.toPlainText())
    a[2][3] = str2int (ui_screen.box22.toPlainText())
    a[2][4] = str2int (ui_screen.box23.toPlainText())
    a[2][5] = str2int (ui_screen.box24.toPlainText())
    a[2][6] = str2int (ui_screen.box25.toPlainText())
    a[2][7] = str2int (ui_screen.box26.toPlainText())
    a[2][8] = str2int (ui_screen.box27.toPlainText())

    a[3][0] = str2int (ui_screen.box28.toPlainText())
    a[3][1] = str2int (ui_screen.box29.toPlainText())
    a[3][2] = str2int (ui_screen.box30.toPlainText())
    a[3][3] = str2int (ui_screen.box31.toPlainText())
    a[3][4] = str2int (ui_screen.box32.toPlainText())
    a[3][5] = str2int (ui_screen.box33.toPlainText())
    a[3][6] = str2int (ui_screen.box34.toPlainText())
    a[3][7] = str2int (ui_screen.box35.toPlainText())
    a[3][8] = str2int (ui_screen.box36.toPlainText())

    a[4][0] = str2int (ui_screen.box37.toPlainText())
    a[4][1] = str2int (ui_screen.box38.toPlainText())
    a[4][2] = str2int (ui_screen.box39.toPlainText())
    a[4][3] = str2int (ui_screen.box40.toPlainText())
    a[4][4] = str2int (ui_screen.box41.toPlainText())
    a[4][5] = str2int (ui_screen.box42.toPlainText())
    a[4][6] = str2int (ui_screen.box43.toPlainText())
    a[4][7] = str2int (ui_screen.box44.toPlainText())
    a[4][8] = str2int (ui_screen.box45.toPlainText())

    a[5][0] = str2int (ui_screen.box46.toPlainText())
    a[5][1] = str2int (ui_screen.box47.toPlainText())
    a[5][2] = str2int (ui_screen.box48.toPlainText())
    a[5][3] = str2int (ui_screen.box49.toPlainText())
    a[5][4] = str2int (ui_screen.box50.toPlainText())
    a[5][5] = str2int (ui_screen.box51.toPlainText())
    a[5][6] = str2int (ui_screen.box52.toPlainText())
    a[5][7] = str2int (ui_screen.box53.toPlainText())
    a[5][8] = str2int (ui_screen.box54.toPlainText())

    a[6][0] = str2int (ui_screen.box55.toPlainText())
    a[6][1] = str2int (ui_screen.box56.toPlainText())
    a[6][2] = str2int (ui_screen.box57.toPlainText())
    a[6][3] = str2int (ui_screen.box58.toPlainText())
    a[6][4] = str2int (ui_screen.box59.toPlainText())
    a[6][5] = str2int (ui_screen.box60.toPlainText())
    a[6][6] = str2int (ui_screen.box61.toPlainText())
    a[6][7] = str2int (ui_screen.box62.toPlainText())
    a[6][8] = str2int (ui_screen.box63.toPlainText())

    a[7][0] = str2int (ui_screen.box64.toPlainText())
    a[7][1] = str2int (ui_screen.box65.toPlainText())
    a[7][2] = str2int (ui_screen.box66.toPlainText())
    a[7][3] = str2int (ui_screen.box67.toPlainText())
    a[7][4] = str2int (ui_screen.box68.toPlainText())
    a[7][5] = str2int (ui_screen.box69.toPlainText())
    a[7][6] = str2int (ui_screen.box70.toPlainText())
    a[7][7] = str2int (ui_screen.box71.toPlainText())
    a[7][8] = str2int (ui_screen.box72.toPlainText())

    a[8][0] = str2int (ui_screen.box73.toPlainText())
    a[8][1] = str2int (ui_screen.box74.toPlainText())
    a[8][2] = str2int (ui_screen.box75.toPlainText())
    a[8][3] = str2int (ui_screen.box76.toPlainText())
    a[8][4] = str2int (ui_screen.box77.toPlainText())
    a[8][5] = str2int (ui_screen.box78.toPlainText())
    a[8][6] = str2int (ui_screen.box79.toPlainText())
    a[8][7] = str2int (ui_screen.box80.toPlainText())
    a[8][8] = str2int (ui_screen.box81.toPlainText())

    if checkvalidity(a) and solve(a):
        ui_screen.box1.setPlainText(str(a[0][0]))
        ui_screen.box2.setPlainText(str(a[0][1]))
        ui_screen.box3.setPlainText(str(a[0][2]))
        ui_screen.box4.setPlainText(str(a[0][3]))
        ui_screen.box5.setPlainText(str(a[0][4])) 
        ui_screen.box6.setPlainText(str(a[0][5])) 
        ui_screen.box7.setPlainText(str(a[0][6])) 
        ui_screen.box8.setPlainText(str(a[0][7])) 
        ui_screen.box9.setPlainText(str(a[0][8])) 


        ui_screen.box10.setPlainText(str(a[1][0])) 
        ui_screen.box11.setPlainText(str(a[1][1])) 
        ui_screen.box12.setPlainText(str(a[1][2])) 
        ui_screen.box13.setPlainText(str(a[1][3])) 
        ui_screen.box14.setPlainText(str(a[1][4])) 
        ui_screen.box15.setPlainText(str(a[1][5])) 
        ui_screen.box16.setPlainText(str(a[1][6])) 
        ui_screen.box17.setPlainText(str(a[1][7])) 
        ui_screen.box18.setPlainText(str(a[1][8])) 

        ui_screen.box19.setPlainText(str(a[2][0])) 
        ui_screen.box20.setPlainText(str(a[2][1])) 
        ui_screen.box21.setPlainText(str(a[2][2])) 
        ui_screen.box22.setPlainText(str(a[2][3])) 
        ui_screen.box23.setPlainText(str(a[2][4])) 
        ui_screen.box24.setPlainText(str(a[2][5])) 
        ui_screen.box25.setPlainText(str(a[2][6])) 
        ui_screen.box26.setPlainText(str(a[2][7])) 
        ui_screen.box27.setPlainText(str(a[2][8])) 

        ui_screen.box28.setPlainText(str(a[3][0])) 
        ui_screen.box29.setPlainText(str(a[3][1])) 
        ui_screen.box30.setPlainText(str(a[3][2])) 
        ui_screen.box31.setPlainText(str(a[3][3])) 
        ui_screen.box32.setPlainText(str(a[3][4])) 
        ui_screen.box33.setPlainText(str(a[3][5])) 
        ui_screen.box34.setPlainText(str(a[3][6])) 
        ui_screen.box35.setPlainText(str(a[3][7])) 
        ui_screen.box36.setPlainText(str(a[3][8])) 

        ui_screen.box37.setPlainText(str(a[4][0])) 
        ui_screen.box38.setPlainText(str(a[4][1])) 
        ui_screen.box39.setPlainText(str(a[4][2])) 
        ui_screen.box40.setPlainText(str(a[4][3])) 
        ui_screen.box41.setPlainText(str(a[4][4])) 
        ui_screen.box42.setPlainText(str(a[4][5])) 
        ui_screen.box43.setPlainText(str(a[4][6])) 
        ui_screen.box44.setPlainText(str(a[4][7])) 
        ui_screen.box45.setPlainText(str(a[4][8])) 

        ui_screen.box46.setPlainText(str(a[5][0])) 
        ui_screen.box47.setPlainText(str(a[5][1])) 
        ui_screen.box48.setPlainText(str(a[5][2])) 
        ui_screen.box49.setPlainText(str(a[5][3])) 
        ui_screen.box50.setPlainText(str(a[5][4])) 
        ui_screen.box51.setPlainText(str(a[5][5])) 
        ui_screen.box52.setPlainText(str(a[5][6])) 
        ui_screen.box53.setPlainText(str(a[5][7])) 
        ui_screen.box54.setPlainText(str(a[5][8])) 

        ui_screen.box55.setPlainText(str(a[6][0])) 
        ui_screen.box56.setPlainText(str(a[6][1])) 
        ui_screen.box57.setPlainText(str(a[6][2])) 
        ui_screen.box58.setPlainText(str(a[6][3])) 
        ui_screen.box59.setPlainText(str(a[6][4])) 
        ui_screen.box60.setPlainText(str(a[6][5])) 
        ui_screen.box61.setPlainText(str(a[6][6])) 
        ui_screen.box62.setPlainText(str(a[6][7])) 
        ui_screen.box63.setPlainText(str(a[6][8])) 

        ui_screen.box64.setPlainText(str(a[7][0])) 
        ui_screen.box65.setPlainText(str(a[7][1])) 
        ui_screen.box66.setPlainText(str(a[7][2])) 
        ui_screen.box67.setPlainText(str(a[7][3])) 
        ui_screen.box68.setPlainText(str(a[7][4])) 
        ui_screen.box69.setPlainText(str(a[7][5])) 
        ui_screen.box70.setPlainText(str(a[7][6])) 
        ui_screen.box71.setPlainText(str(a[7][7])) 
        ui_screen.box72.setPlainText(str(a[7][8])) 

        ui_screen.box73.setPlainText(str(a[8][0])) 
        ui_screen.box74.setPlainText(str(a[8][1])) 
        ui_screen.box75.setPlainText(str(a[8][2])) 
        ui_screen.box76.setPlainText(str(a[8][3])) 
        ui_screen.box77.setPlainText(str(a[8][4])) 
        ui_screen.box78.setPlainText(str(a[8][5])) 
        ui_screen.box79.setPlainText(str(a[8][6])) 
        ui_screen.box80.setPlainText(str(a[8][7])) 
        ui_screen.box81.setPlainText(str(a[8][8])) 
        QMessageBox.information(mainscreen,"Puzzle Solved Successfully","SUdoku puzzle has been solved")
    else:
        QMessageBox.warning(mainscreen,'Invalid puzzle','Provided sudoku puzzle is unsolvable')



if __name__ == "__main__":
    
    mainscreen.show()
    ui_main.Start_Button.clicked.connect(shownextscreen)
    ui_screen.pushButton.clicked.connect(startsolving)
    loader_img = QMovie("giphy.gif")
    ui_main.background.setMovie(loader_img)
    ui_main.background2.setMovie(loader_img)
    loader_img.setScaledSize(ui_main.background.size())
    loader_img.start()
    
    sys.exit(app.exec_())
