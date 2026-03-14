'''
def LR_k_place(arr):
    k = 3
    n = len(arr)
    temp = arr[0:k]

    for i in range(k,n):
        arr[i-k]=arr[i]

        arr[n-k:]=temp
    return arr
arr = [1,2,3,4,5]
print(LR_k_place(arr))    

'''

# optimal approach
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def leftRotate(arr, k):
    n = len(arr)
    k = k % n

    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)

    return arr


arr = [1,2,3,4,5]
print(leftRotate(arr,2))