import re
less_than="<"
greater_than=">"
inpt=input("Enter your inequality to see if it is true or not: ")
temp = re.findall(r'\d+', inpt)
res = list(map(int, temp))
try:
    if res[0]>res[1] and greater_than in inpt:
        print("True")
    else:
        print("False")
    exit()

    if res[0]<res[1] and less_than in inpt:
        print("True")
    else:
        print("False")
    exit()
except:
    print("Not a valid input")
