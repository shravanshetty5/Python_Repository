#Sudoku checker program... Well almost.
#Program takes any nxn matrix and checks for sudoku condition.
#i.e. repetition in rows or columns but not inside a sub square.

def check_sudoku(x):
    z= zip(*x) #Transpose Matrix of x
    l = len(x) #get matrix dimention
    c_list = range(1,l+1) #get list of numbers to check against
    for i in x:
        if len(i)!=len(set(i)):#checks if all elements are distinct in row
            return False
        for k in i:
            if k not in c_list: #Checks if all elements are numbers
                return False
    for j in z:
        if len(j)!=len(set(j)):#checks if all elements are distinct in column
            return False
    return True
