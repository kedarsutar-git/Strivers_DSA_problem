'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
#for i in range(5):
 #   for j in range(5):
 #       print("*",end=" ")
  #  print()  



'''
*
**
***
****
*****
'''    

#for i in range(5):
#    for j in range(i+1):
#        print("*",end="")

#    print()    




'''
1
12
123
1234
12345
'''   

#for i in range(5):
#    for j in range(i+1):
#        print(j+1,end="")

#    print()    




'''
1
22
333
4444
55555
'''

#for i in range(5):
#    for j in range(i+1):
#        print(i+1,end="")

#    print()    



'''
*****
****
***
**
*
'''  
#for i in range(6,0,-1):
#    for j in range(i-1):
#        print("*",end="")

#    print()     




'''
12345
1234
123
12
1
'''
for i in range(6,0,-1):
    for j in range(i-1):
        print(j+1,end="")

    print() 



n = 7
for i in range(n-4):
    for j in range(n-5+i):
        print("*",end=" ")

    for j in range(n-5-i):
        print(" ",end=" ")

    for j in range(n-5+i):
        print("*",end=" ")

    print()

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")

    for j in range(n-i):
        print(" ",end=" ")

    for j in range(i):
        print("*",end= " ") 
    print()                       