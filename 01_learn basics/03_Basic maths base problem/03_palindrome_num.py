n = int(input("Enter the number:"))
rev = 0
dup = n
while(n>0):
    m = n%10
    n = n//10
    rev = (rev*10) + m
print(rev)    
if(rev == dup):
      print("The  number is palindrome")

else:
    print("The number is not palindrome")    

'''
Time Complexity:O(logn)
Space Complexity:O(1)
'''