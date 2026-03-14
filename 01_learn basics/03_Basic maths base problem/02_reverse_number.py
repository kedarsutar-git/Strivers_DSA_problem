num = int(input("Enter the number:"))

reversed = 0
while(num>0):
    m = num%10
    num = num//10
    
    reversed = (reversed*10) + m

    print(reversed)

