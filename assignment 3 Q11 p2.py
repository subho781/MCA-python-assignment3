#WAP to print the following patterns using loop


num = 3
for i in range(0, num):
    for j in range(0, i):
        print(" ", end="")
    for k in range(0, (num-i)*2 - 1):
        print("*", end="")
    print()