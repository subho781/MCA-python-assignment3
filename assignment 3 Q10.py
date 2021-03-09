#WAP to print the following patterns using loop

def pypart(n):
	for i in range(n, 0,-1):
		for j in range(0, i):
			print("A ",end="")
		print("\r")
n = int(input('enter the number : '))
pypart(n)
