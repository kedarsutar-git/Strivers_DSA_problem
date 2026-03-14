def LeftRotate(arr):
    n = len(arr)
    temp = arr[0]

    for i in range(n-1):
        arr[i] = arr[i+1]


    arr[n-1] = temp
    return arr
arr = [1,2,3,4,5]
print(LeftRotate(arr))
