import math
e = 2.718281
x=int(input("Click 1 for logarithms or click 2 for natural logarithms"))
if x == 1:
    logbase= int(input("Base of logarithm: "))
    num= int(input("Number 2: "))
    print(math.log(num,logbase))
if x == 2:
    num2= int(input("Enter number: "))
    print(math.log(e,num2))
