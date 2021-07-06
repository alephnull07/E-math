import cmath
def basic_calculations():
  c=int(input("Choose 1 for addition, 2 for subtraction, 3 for multiplication, 4 for divison, 5 for other: "))
  try:
    if c <= 4 and c >= 1:
      inp1= complex(input("Insert the first complex number: "))
      inp2= complex(input("Insert the second complex number: "))
    if c == 1:
      print(inp1+inp2)
    if c == 2:
     print(inp1-inp2)
    if c == 3:
      print(inp1*inp2)
    if c == 4:
     print(inp1/inp2)
    if c == 5:
      d = int(input("1 for distance, 2 for polar conversion, 3 for midpoint, 4 for i^any number: "))
      if d == 1:
        yinp1 = complex(input("Insert first point on the complex plane: "))
        yinp2 = complex(input("Insert second point on the complex plane: "))
        val = (yinp1 - yinp2)
        final = abs(val)
        print(f"The distance is about {final} units")
      if d == 2:
        polar_conv = complex(input("Enter the complex number you want to convert"))
        fin = cmath.polar(polar_conv)
        print(fin)
      if d == 3:
        midinp1 = complex(input("Enter first complex number on the complex plane: "))
        midinp2= complex(input("Enter second complex number on the plane"))
        mid=((midinp2+midinp1)/(2))
        print(mid)
      if d == 4:
        i=cmath.sqrt(-1)
        iinp=("What would you want x to be in i^x: ")
        finali=(i**x)
        print(f"The answer is {finali}")
  except:
    print("Please input values as z+j")
    basic_calculations()
  basic_calculations()

basic_calculations()

