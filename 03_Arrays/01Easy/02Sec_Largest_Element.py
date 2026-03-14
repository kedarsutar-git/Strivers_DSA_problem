def second_largest(arr):
    largest = arr[0]
    sec = -1
    n = len(arr)

    for i in range(1,n):
        if(arr[i]>largest):
            sec = largest
            largest = arr[i]

        elif(arr[i]>sec and arr[i]!=largest):
            sec = arr[i]
arr = [23,54,34,446,78,1]
print(second_largest(arr))       



