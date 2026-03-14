n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
small = min(n1,n2)
for i in range(small,0,-1):
    if(n1 % i == 0 and n2 %i ==0):
        print(i)
        break


    