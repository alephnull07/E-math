import math
print("There are no trig identities because they are important for you!!")
type=int(input("Press 1 to use Trig functions; 2 for Pythagorean theorem; 3 for law of sines; 4 for law of cosines; 5 for Any Triangle area: "))

def Pythagorean():
    if type == 2:
        x = int(input("Number 1: "))
        y = int(input("Number 2: "))
        print(math.hypot(x, y))
Pythagorean()

def Trig():
    if type == 1:
        x=int(input('''Press 1 for sin; 2 for cos; 3 for tan; 4 for sin inverse; 5 for cos inverse; 6 for tan inverse: '''))
        if x==1:
            a = int(input("Degree: "))
            b = math.radians(a)
            print(math.sin(b))
        elif x==2:
            a = int(input("Degree: "))
            b = math.radians(a)
            print(math.cos(b))
        elif x==3:
            a = int(input("Degree: "))
            b = math.radians(a)
            print(math.tan(b))
        elif x==4:
            a = float(input("Number: "))
            b=math.asin(a)
            print(math.degrees(b))
        elif x==5:
            a = float(input("Number: "))
            b = math.acos(a)
            print(math.degrees(b))
        else:
            a = float(input("Number: "))
            b = math.atan(a)
            print(math.degrees(b))
Trig()

def law_of_sines():
    if type==3:
        y=int(input("What are you trying to find; press 1 for Angle 1; 2 for opposite leg 1; 3 for angle 2; 4 for opposite 2: "))
        if y==1:
            b = int(input("Opposite Leg 1: "))
            c = math.sin(math.radians(int(input("Angle 2: "))))
            d = int(input("Opposite Leg 2: "))
            print("Angle 1 is: " + str(math.degrees(math.asin((b * c) / d))))
        elif y==2:
            a = math.sin(math.radians(int(input("Angle 1: "))))
            c = math.sin(math.radians(int(input("Angle 2: "))))
            d = int(input("Opposite Leg 2: "))
            print("Opposite leg 1 is: "+str((d*a)/c))
        elif y==3:
            a = math.sin(math.radians(int(input("Angle 1: "))))
            b = int(input("Opposite Leg 1: "))
            d = int(input("Opposite Leg 2: "))
            print("Angle 2 is: " + str(math.degrees(math.asin((d*a)/b))))
        else:
            a = math.sin(math.radians(int(input("Angle 1: "))))
            b = int(input("Opposite Leg 1: "))
            c = math.sin(math.radians(int(input("Angle 2: "))))
            print("Opposite leg 1 is: " + str(math.degrees(math.asin((b*c)/a))))
law_of_sines()

def law_of_cosines():
    if type==4:
        b = int(input("Number b: "))
        c = int(input("Number c: "))
        a = int(input("Number a: "))
        print("Angle A: " + str(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / 2 * b * c))))
law_of_cosines()

def area_triangle():
    if type==5:
        a = int(input("Side 1: "))
        b = int(input("Side 2: "))
        c = int(input("Side 3: "))
        s = (a + b + c) / 2
        print(math.sqrt(s * (s - a) * (s - b) * (s - c)))
area_triangle()
