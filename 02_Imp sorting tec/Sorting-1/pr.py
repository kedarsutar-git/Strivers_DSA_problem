def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index = j

                temp = arr[i]
                arr[i] = arr[min_index]
                arr[min_index] = temp

    return arr
arr = [12,34,57,78,56]
print(SelectionSort(arr))            
              

