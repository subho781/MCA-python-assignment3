#WAP to print the following patterns using loop

def pypart(n):
    count = 0
    for i in range(0,n):
        for j in range(0, i+1):
            count+=1
            print(count,end=" ")
        print("\r")
n = int(input('enter the number : '))
pypart(n)
