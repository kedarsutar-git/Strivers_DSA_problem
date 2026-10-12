n = 10

for i in range(n):
    
    # K
    for j in range(n):
        if j == 0 or i + j == 3 or i - j == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end=" ")

    # E
    for j in range(n):
        if i == 0 or i == n//2 or i == n-1 or j == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end=" ")

    # D
    for j in range(n):
        if j == 0 or (j == n-1 and i != 0 and i != n-1) or ((i == 0 or i == n-1) and j < n-1):
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end=" ")

    # A
    for j in range(n):
        if ((j == 0 or j == n-1) and i != 0) or ((i == 0 or i == n//2) and j > 0 and j < n-1):
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end=" ")

    # R
    for j in range(n):
        if j == 0 or (i == 0 and j < n-1) or (i == n//2 and j < n-1) or (j == n-1 and i < n//2 and i != 0) or (i - j == 3):
            print("*", end="")
        else:
            print(" ", end="")
    
    print()


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

    for j in range(2*(n-i)+1):
        print(" ",end="")  

    for j in range(i,0,-1):
        print(j,end="")      
    print() 

