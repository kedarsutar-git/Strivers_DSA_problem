'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
n = 5
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
n = 5 
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()       

'''
1
12
123
1234
12345
'''
n = 5 
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
n = 5 
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
n = 5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()    


'''
12345
1234
123
12
1
'''
n = 5 
for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()    


'''n = 5
        *
       ***
      *****
     *******
    *********

'''
n = 5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")

    for j in range((2*i)-1):
        print("*",end="")

    for j in range(n-i):
        print(" ",end="")
    print()        


'''
    *********
     *******
      *****
       ***
        *
'''

'''
            *
           ***
          *****
         *******
        *********
        *********
         *******
          *****
           ***
            *

'''
'''
*
**
*** 
****
*****
****
***
**
*
'''

'''
1      1
12    21
123  321
12344321
'''
n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    for j in range(2*n-(2*i+2)):
        print(" ",end="")
    for j in range(i+1):
        print(j+1,end="")
    print()    
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
n = 5
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num +=1


    print()    

'''
* * * *
*     *
*     *
* * * *
'''
n = 5
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or j == n-1 or i == n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            

'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''
n = 5
for i in range(n):
    for j in range(i+1):
        x = i+j
        if(x%2==0):
            print("1",end=" ")

        else:
            print("0",end=" ")

    print()        