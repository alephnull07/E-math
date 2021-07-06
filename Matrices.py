x=int(input("Press 1 for Add, 2 for subtract, 3 for multiply: "))
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
    elif x == 2:
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
    else:
        return 0
addandsubMatrix()

def multMatrix():
    if x == 3:
        for z in Matrix1:
            FinalMatrix1 = []
            for a in z:
                j=0
                FinalMatrix2=[]
                while j<columnMatrix2:
                    v=0
                    while v<rowMatrix2:
                        FinalMatrix2.append(int(a)*int(Matrix2[v][j]))
                        v=v+1
                    j=j+1
                FinalMatrix1.append(FinalMatrix2)
            #Start
            FinalMatrix3=[]
            a=0
            while a<len(FinalMatrix1):
                b=0
                FinalMatrix4=[]
                while b < len(FinalMatrix1[a]):
                    FinalMatrix4.append(int(FinalMatrix1[a][b+a]))
                    b = b + int(len(FinalMatrix1[a]) / len(FinalMatrix1))
                FinalMatrix3.append(FinalMatrix4)
                a=a+1
            c=0
            FinalMatrix5=[]
            while c<len(FinalMatrix3):
                d=0
                FinalMatrix6=0
                while d<len(FinalMatrix3[c]):
                    FinalMatrix6=FinalMatrix6+FinalMatrix3[d][c]
                    d=d+1
                FinalMatrix5.append(FinalMatrix6)
                c=c+1
            print(FinalMatrix5)
multMatrix()
