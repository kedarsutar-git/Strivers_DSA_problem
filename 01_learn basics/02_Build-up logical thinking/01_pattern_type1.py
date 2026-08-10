'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()  



'''
*
**
***
****
*****
'''    
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")

    print()    




'''
1
12
123
1234
12345
'''   
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")

    print()    




'''
1
22
333
4444
55555
'''
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(i+1):
        print(i+1,end="")

    print()    



'''
*****
****
***
**
*
'''  
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(n-i):
        print("*",end="")

    print()     

'''
12345
1234
123
12
1
'''


