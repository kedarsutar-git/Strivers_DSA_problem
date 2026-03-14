'''
     *
    * *
   * * *
  * * * *
 * * * * *
'''
#n = int(input("Enter the number:"))
#for i in range(n):
#    for j in range(i,n):
#        print(" ",end=" ")

#    for k in range(i):
#        print("*",end=" ")

#    for l in range(i,1,-1):
#        print("*",end=" ")

#    print(" ")            




'''n = 5
        *
       ***
      *****
     *******
    *********

'''
#N = 5
#for i in range(N):

            # Print leading spaces
#            for j in range(N - i - 1):
#                print(" ", end="")

            # Print stars
#            for j in range(2 * i + 1):
#                print("*", end="")

            # Print trailing spaces
#            for j in range(N - i - 1):
#                print(" ", end="")

            # Move to next row
#            print()





'''
    *********
     *******
      *****
       ***
        *
'''
#N = 7
#for i in range(N):
#    for j in range(i):
#        print(" ",end=" ")

#    for j in range(2*N-(2*i+1)):
#        print("*",end=" ")

#    for j in range(i):
#        print(" ",end=" ")

#    print(" ")            





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
#n = 9
#for i in range(n):
#    for j in range(n -i-1):
#        print(" ",end=" ")

#    for j in range(2*i+1):
#        print("*",end=" ")

#    for j in range(n -i -1):
#        print(" ",end=" ")
#    print(" ")    

#for i in range(n):
#    for k in range(i):
#        print(" ",end=" ")

#    for k in range(2*n-(2*i+1)):
#        print("*",end=" ")

#    for k in range(i):
#        print(" ",end=" ")

#    print("")                            





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
         
#N = 5
#for i in range(1, 2 * N):
    
    # stars would be equal to the row no. until first half
#    stars = i
    
    # for the second half of the rotated triangle
#    if i > N:
#        stars = 2 * N - i
    
    # printing stars in each row
#    for j in range(stars):
#        print("*", end="")
    
    # move to next line
#    print()







'''
1      1
12    21
123  321
12344321
'''
n = 5 
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end="")
    print()    



'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''


#n = 5
#num =1
#for i in range(1,n+1):
#     for j in range(1,i+1):
#          print(num,end=" ")
#          num = num+1

#     print("")     






'''
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
'''

#n =  5
#space = 0
#for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
     
#     for j in range(space):
#         print(" ",end=" ")

#     for j in range(n-i):
#         print("*",end=" ")
#     print("") 
#     space+=2
     
#space = 8

#for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
     
#     for j in range(space):
#         print(" ",end=" ")

#     for j in range(i+1):
#         print("*",end=" ")
#     print("") 
#     space-=2     








'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''
#n = 5
#space = 2*n-2
#for i in range(1,2*n):
#    star =i

#    if(i>n):
#        star = 2*n-i
    # star
#    for j in range(star):
#        print("*",end=" ")        
    
    # space
#    for j in range(space+1):
#        print(" ",end=" ")
     
    # star
#    for j in range(star):
#        print("*",end=" ")  

#    print(" ")

#    if(i<n):
#            space -=2

#    else:
#        space+=2        







'''
* * * *
*     *
*     *
* * * *
'''
n = 4
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end="")    

        else:
            print(" ",end="")

    print()              







'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

i+j = even : 1
i+j = odd  : 0
'''

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        x = i+j
        if(x%2==0):
            print("1",end="")

        else:
            print("0",end="") 

    print()        

