import math
x=int(input("Press 1 for Add, 2 for subtract, 3 for multiply, 4 to find determinant: "))
#may break if it is a letter is entered
if int(x)<1 or int(x)>5:
    print("invalid number")
#may break if a letter is entered

rowMatrix1=int(input("How many rows does your Matrix 1 have? "))
columnMatrix1=int(input("How many columns does your Matrix 1 have? "))
rowMatrix2=int(input("How many rows does your Matrix 2 have? "))
columnMatrix2=int(input("How many columns does your Matrix 2 have? "))

Matrix1=[]
a=1
while a<=rowMatrix1:
    b=1
    FirstMatrix=[]
    while b<=columnMatrix1:
        d=int(input("Matrix 1; Row "+str(a)+"; Number "+str(b)+": "))
        FirstMatrix.append(d)
        b=b+1
    Matrix1.append(FirstMatrix)
    a=a+1

Matrix2=[]
c=1
while c<=rowMatrix2:
    d=1
    SecondMatrix=[]
    while d<=columnMatrix2:
        e=int(input("Matrix 2; Row "+str(c)+"; Number "+str(d)+": "))
        SecondMatrix.append(e)
        d=d+1
    Matrix2.append(SecondMatrix)
    c=c+1

def addandsubMatrix():
    if x == 1:
        try:
            a = 0
            FinalMatrix = []
            while a < rowMatrix1 or a < rowMatrix2:
                b = 0
                FMatrix = []
                while b < columnMatrix1 or b < columnMatrix2:
                    FMatrix.append(int(Matrix1[a][b]) + int(Matrix2[a][b]))
                    b = b + 1
                FinalMatrix.append(FMatrix)
                a = a + 1
            for n in FinalMatrix:
                print(n)
        except:
            print("The number of rows and columns in both Matrices have to be the same, like Matrix1 is 2*3 and Matrix2 is 2*3")
    elif x == 2:
        try:
            a = 0
            FinalMatrix = []
            while a < rowMatrix1 or a < rowMatrix2:
                b = 0
                FMatrix = []
                while b < columnMatrix1 or b < columnMatrix2:
                    FMatrix.append(int(Matrix1[a][b]) - int(Matrix2[a][b]))
                    b = b + 1
                FinalMatrix.append(FMatrix)
                a = a + 1
            for n in FinalMatrix:
                print(n)
        except:
            print("The number of rows and columns in both Matrices have to be the same, like Matrix1 is 2*3 and Matrix2 is 2*3")
addandsubMatrix()

def multMatrix():
    if x == 3:
        if rowMatrix1!=columnMatrix2:
            print("The number of rows in Matrix1 has to be the same as the number of columns in Matrix2. ")
        FinalMatrix1 = []
        row1 = 0
        while row1 < rowMatrix1:
            column2 = 0
            while column2 < columnMatrix2:
                column1 = 0
                row2 = 0
                while column1 < columnMatrix1 and row2 < rowMatrix2:
                    FinalMatrix1.append(Matrix1[row1][column1] * Matrix2[row2][column2])
                    row2 += 1
                    column1 += 1
                column2 += 1
            row1 += 1
        FinalMatrix2 = []
        cdc = 0
        abc = 0
        sum = 0
        while cdc < len(FinalMatrix1):
            if abc > math.sqrt(columnMatrix1 * rowMatrix2) - 1:
                abc = 0
                sum = 0
            sum += FinalMatrix1[cdc]
            FinalMatrix2.append(sum)
            abc += 1
            cdc += 1
        FinalMatrix3 = []
        i = math.sqrt(columnMatrix1 * rowMatrix2) - 1
        while i < len(FinalMatrix2):
            FinalMatrix3.append(FinalMatrix2[int(i)])
            i += math.sqrt(columnMatrix1 * rowMatrix2)
        FinalMatrix4 = []
        i = 0
        cdd = 0
        while i < len(FinalMatrix3):
            FinalMatrix4.append(FinalMatrix3[i])
            if cdd == math.sqrt(rowMatrix1 * columnMatrix2) - 1:
                print(FinalMatrix4)
                FinalMatrix4 = []
                cdd = 0
            else:
                cdd += 1
            i += 1
multMatrix()

def determinant():
    if x==4:
        if rowMatrix1==2 and columnMatrix1==2:
            print("Determinant for Matrix 1 is: "+str(Matrix1[0][0]*Matrix1[1][1]-Matrix1[1][0]*Matrix1[0][1]))
        if rowMatrix1==3 and columnMatrix1==3:
            print("Determinant for Matrix 1 is: "+str((Matrix1[0][0]*Matrix1[1][1]*Matrix1[2][2]+Matrix1[0][1]*Matrix1[1][2]*Matrix1[2][0]+Matrix1[0][2]*Matrix1[1][0]*Matrix1[2][1])-(Matrix1[2][0]*Matrix1[1][1]*Matrix1[0][2]+Matrix1[2][1]*Matrix1[1][2]*Matrix1[0][0]+Matrix1[2][2]*Matrix1[1][0]*Matrix1[0][1])))
        if rowMatrix1==2 and columnMatrix1==2:
            print("Determinant for Matrix 2 is: "+str(Matrix1[0][0]*Matrix1[1][1]-Matrix1[1][0]*Matrix1[0][1]))
        if rowMatrix1==3 and columnMatrix1==3:
            print("Determinant for Matrix 2 is: "+str((Matrix1[0][0]*Matrix1[1][1]*Matrix1[2][2]+Matrix1[0][1]*Matrix1[1][2]*Matrix1[2][0]+Matrix1[0][2]*Matrix1[1][0]*Matrix1[2][1])-(Matrix1[2][0]*Matrix1[1][1]*Matrix1[0][2]+Matrix1[2][1]*Matrix1[1][2]*Matrix1[0][0]+Matrix1[2][2]*Matrix1[1][0]*Matrix1[0][1])))
        else:
            print("The number of rows must be same as the number of columns in both Matrices, like 2*2, or 3*3, not 2*3")
determinant()
