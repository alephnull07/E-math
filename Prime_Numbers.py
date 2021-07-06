x=int(input("Prime Numbers Under: "))
def check(a):
    for x in range(2,a):
        if a % x==0:
            return 0
    print(a)
for i in range(2,x+1):
    check(i)
