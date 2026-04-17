'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()  



'''
*
**
***
****
*****
'''    

for i in range(5):
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

for i in range(5):
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

for i in range(5):
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
for i in range(6,0,-1):
    for j in range(i-1):
        print("*",end="")

    print()     




'''
12345
1234
123
12
1
'''
n = int(input("Enter the number:"))
for i in range(n+1,0,-1):
    for j in range(i-1):
        print(j+1,end="")

    print() 



'''
1
21
321
4321
'''
n = int(input("Enter the number:"))
for i in range(0,n):
    for j in range(i+1,0,-1):
        print(j,end="")
    print()




'''
1
2 3
4 5 6
7 8 9 10
'''
n = int(input("Enter the number:"))
num = 1
for i in range(n):
    for j in range(i+1,0,-1):
        print(num,end="")
        num = num+1

    print()    



'''

     *
    * *
   * * *
  * * * *
 * * * * *

'''
for i in range(5):
    for j in range(i,5):
        print(" ",end=" ")

    for k in range(i):
        print("*",end=" ")

    for m in range(i,1,-1):
        print("*",end=" ")
    print(" ")            



