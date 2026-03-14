# Brute force approach
def union(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    s = set()

    for i in range(n1):
        s.add(arr1[i])

    for i in range(n2):
        s.add(arr2[i])   

    l = list(set(s))     

    return l

arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,5,6]

print(union(arr1,arr2))

# optimal approach



