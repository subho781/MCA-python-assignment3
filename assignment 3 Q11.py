#WAP to print the following patterns using loop

def pypart(n):
    for i in range(1, n+1):
        for k in range(0,n-i+1):
            print(" ",end="")
        for j in range(0, i*2 -1):
            print("*",end="")
        print("\r")
n = int(input('enter the number : '))
pypart(n)
