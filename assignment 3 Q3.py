# WAP to print natural number from 1 to n 

number = int(input("Please Enter any Number: "))
i = 1

print("The List of Natural Numbers from 1 to {} are".format(number)) 

while ( i <= number):
    print (i, end='  ')
    i = i + 2
