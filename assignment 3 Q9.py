#WAP to display all the prime number upto n


num = int(input('enter the number: '))
count = 0
for i in range(num+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else:
        count += 1
        print(i, end=' ') 
print("\nTotal prime number is :",str(count))