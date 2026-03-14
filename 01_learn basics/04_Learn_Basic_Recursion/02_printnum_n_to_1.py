def num(n):
    if(n==1):
        return 1
    print(n)
    print(num(n-1))
print(num(4))      
