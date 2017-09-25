
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
     
"""" 
 