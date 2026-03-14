n = int(input("Enter the number:"))
sum=0
dup = n
order = len(str(n))

while(n>0):
    digits = n%10
    sum+= digits**order
    n = n//10
if(sum==dup):
    print("The number is armstrong")
   

else:
    print("The number is not armstrong")    

