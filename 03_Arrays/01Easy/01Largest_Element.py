def largest(arr):
    n = len(arr)
    largest = arr[0]
    for i in range(1,n):
        if(arr[i]>largest):
            largest = arr[i]

    return largest
arr = [12,34,56,4,3,56,778,55]
print(largest(arr))        


