n = 5
for i in range(n):
    for j in range(i+1):
        m = i+j
        if(m%2==0):
            print("1",end=" ")

        else:
            print("0",end=" ")

    print( )

'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 

'''    


n = 6
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()        

'''
* * * * * *
*         *
*         *
*         *
*         *
* * * * * *
'''

n = 9
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")

 
    for j in range(2*(n-i)):
        print(" ",end="")

       
    for j in range(i):
        print("*",end="")

    print()

for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")

    for j in range(2*(n-i)):
        print(" ",end="")

    for j in range(i):
        print("*",end="")

    print()    

    '''
*                *
**              **
***            ***
****          ****
*****        *****
******      ******
*******    *******
********  ********
******************
******************
********  ********
*******    *******
******      ******
*****        *****
****          ****
***            ***
**              **
*                *

    '''


n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")

    for j in range(n):
        print("*",end="")        

    print()    

'''     
    *****
   *****
  *****
 *****
*****

'''


n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(i,end=" ")       
    print()    

    '''
    1
   2 2 
  3 3 3
 4 4 4 4
5 5 5 5 5
    '''


n = 5
for i in range(1,n):
    for j in range(n-i):
        print(" ",end="")

    for j in range(i,0,-1):
        print(j,end="") 


    for j in range(2,i+1):
        print(j,end="")        
    print()  

'''
    1
   212
  32123
 4321234
'''
n =4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")

    for j in range((2*i)-1):
        print("*",end=" ") 

    for j in range(1,n+1):
        print(" ",end=" ")      
    print()     
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")

    for j in range((2*i)-1):
        print("*",end=" ") 

    for j in range(1,n+1):
        print(" ",end=" ")      
    print()      

'''
   *
  ***
 *****
*******    
*******
 *****
  ***
   *
'''   

n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print("",end=" ")

    for j in range(i):
        print(i,end=" ")    

    print()