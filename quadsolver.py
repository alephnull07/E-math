quad = input("Type your quadratic with no spaces")
indexes = []
for y in range(0, len(quad)):
    if quad[y] == "x":
        indexes.append(y)
a = (quad[0:indexes[0]])
if len(a) == 0:
    a = 1
else:
    a = int(a)


b = quad[(indexes[0]+3) :indexes[1]]

if len(b) == 1:
    b = 1
else:
    b = int(b)
c = quad[(indexes[1] +1) ::]
if len(c) == 0:
    c = 0
else:
    c = int(c)

x = (-b + ((b**2 + (4*a*c * -1))**0.5))/(2*a)
y = (-b - ((b**2 + (4*a*c * -1))**0.5))/(2*a)
print("the simplified versions are: " + str(x) +" and " + str(y))

