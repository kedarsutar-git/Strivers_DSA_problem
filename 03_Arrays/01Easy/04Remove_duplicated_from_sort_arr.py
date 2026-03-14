def check(arr):
    n = len(arr)
    if(n==0):
        return 0
    i = 0
    for j in range(1,n):
        if(arr[i]!=arr[j]):
           i = i+1    
           arr[i]=arr[j]


    return i+1
arr = [1,1,2,2,3,3,3,4] 
print(arr[:check(arr)])   



# using set method
def Remove(arr):
    s = set()
    for num in arr:
        s.add(num)
    l = list(set(s))

    return l
arr = [1,1,2,2,3,3,3,4] 

print(Remove(arr))
    

