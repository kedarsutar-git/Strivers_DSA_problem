def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]        # element to be inserted
        j = i - 1

        # move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # insert key at correct position
        arr[j + 1] = key

    return arr

arr = [12,34,56,21,43,54] 
print(insertion_sort(arr))       
 




