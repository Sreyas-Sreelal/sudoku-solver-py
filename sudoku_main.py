import sys
from gui_main import mainscreen,ui_main,app
from gui_solver import solver_screen,ui_screen

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
 

def solve(a,i=0,j=0): 

    i,j = UAN(a,i,j)
    if  i == -1: 
         return True 
    for k in range(1,10): 
     
        if safe(a,i,j,k): 
         
            a[i][j] = k; 

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
    solver_screen.show()

def startsolving():
    a[0][0] = int (ui_screen.box1.toPlainText())
    a[0][1] = int (ui_screen.box2.toPlainText())
    a[0][2] = int (ui_screen.box3.toPlainText())
    a[0][3] = int (ui_screen.box4.toPlainText())
    a[0][4] = int (ui_screen.box5.toPlainText())
    a[0][5] = int (ui_screen.box6.toPlainText())
    a[0][6] = int (ui_screen.box7.toPlainText())
    a[0][7] = int (ui_screen.box8.toPlainText())
    a[0][8] = int (ui_screen.box9.toPlainText())

    a[0][0] = int (ui_screen.box10.toPlainText())
    a[1][1] = int (ui_screen.box11.toPlainText())
    a[1][2] = int (ui_screen.box12.toPlainText())
    a[1][3] = int (ui_screen.box13.toPlainText())
    a[1][4] = int (ui_screen.box14.toPlainText())
    a[1][5] = int (ui_screen.box15.toPlainText())
    a[1][6] = int (ui_screen.box16.toPlainText())
    a[1][7] = int (ui_screen.box17.toPlainText())
    a[1][8] = int (ui_screen.box18.toPlainText())

    a[2][0] = int (ui_screen.box19.toPlainText())
    a[2][1] = int (ui_screen.box20.toPlainText())
    a[2][2] = int (ui_screen.box21.toPlainText())
    a[2][3] = int (ui_screen.box22.toPlainText())
    a[2][4] = int (ui_screen.box23.toPlainText())
    a[2][5] = int (ui_screen.box24.toPlainText())
    a[2][6] = int (ui_screen.box25.toPlainText())
    a[2][7] = int (ui_screen.box26.toPlainText())
    a[2][8] = int (ui_screen.box27.toPlainText())

    a[3][0] = int (ui_screen.box28.toPlainText())
    a[3][1] = int (ui_screen.box29.toPlainText())
    a[3][2] = int (ui_screen.box30.toPlainText())
    a[3][3] = int (ui_screen.box31.toPlainText())
    a[3][4] = int (ui_screen.box32.toPlainText())
    a[3][5] = int (ui_screen.box33.toPlainText())
    a[3][6] = int (ui_screen.box34.toPlainText())
    a[3][7] = int (ui_screen.box35.toPlainText())
    a[3][8] = int (ui_screen.box36.toPlainText())

    a[4][0] = int (ui_screen.box37.toPlainText())
    a[4][1] = int (ui_screen.box38.toPlainText())
    a[4][2] = int (ui_screen.box39.toPlainText())
    a[4][3] = int (ui_screen.box40.toPlainText())
    a[4][4] = int (ui_screen.box41.toPlainText())
    a[4][5] = int (ui_screen.box42.toPlainText())
    a[4][6] = int (ui_screen.box43.toPlainText())
    a[4][7] = int (ui_screen.box44.toPlainText())
    a[4][8] = int (ui_screen.box45.toPlainText())

    a[5][0] = int (ui_screen.box46.toPlainText())
    a[5][1] = int (ui_screen.box47.toPlainText())
    a[5][2] = int (ui_screen.box48.toPlainText())
    a[5][3] = int (ui_screen.box49.toPlainText())
    a[5][4] = int (ui_screen.box50.toPlainText())
    a[5][5] = int (ui_screen.box51.toPlainText())
    a[5][6] = int (ui_screen.box52.toPlainText())
    a[5][7] = int (ui_screen.box53.toPlainText())
    a[5][8] = int (ui_screen.box54.toPlainText())

    a[6][0] = int (ui_screen.box55.toPlainText())
    a[6][1] = int (ui_screen.box56.toPlainText())
    a[6][2] = int (ui_screen.box57.toPlainText())
    a[6][3] = int (ui_screen.box58.toPlainText())
    a[6][4] = int (ui_screen.box59.toPlainText())
    a[6][5] = int (ui_screen.box60.toPlainText())
    a[6][6] = int (ui_screen.box61.toPlainText())
    a[6][7] = int (ui_screen.box62.toPlainText())
    a[6][8] = int (ui_screen.box63.toPlainText())

    a[7][0] = int (ui_screen.box64.toPlainText())
    a[7][1] = int (ui_screen.box65.toPlainText())
    a[7][2] = int (ui_screen.box66.toPlainText())
    a[7][3] = int (ui_screen.box67.toPlainText())
    a[7][4] = int (ui_screen.box68.toPlainText())
    a[7][5] = int (ui_screen.box69.toPlainText())
    a[7][6] = int (ui_screen.box70.toPlainText())
    a[7][7] = int (ui_screen.box71.toPlainText())
    a[7][8] = int (ui_screen.box72.toPlainText())

    a[8][0] = int (ui_screen.box73.toPlainText())
    a[8][1] = int (ui_screen.box74.toPlainText())
    a[8][2] = int (ui_screen.box75.toPlainText())
    a[8][3] = int (ui_screen.box76.toPlainText())
    a[8][4] = int (ui_screen.box77.toPlainText())
    a[8][5] = int (ui_screen.box78.toPlainText())
    a[8][6] = int (ui_screen.box79.toPlainText())
    a[8][7] = int (ui_screen.box80.toPlainText())
    a[8][8] = int (ui_screen.box81.toPlainText())

    if solve(a):
        pass

    else:
        pass

    

if __name__ == "__main__":
    
    mainscreen.show()
    ui_main.Start_Button.clicked.connect(shownextscreen)
    ui_screen.pushButton.clicked.connect(startsolving)
    sys.exit(app.exec_())
