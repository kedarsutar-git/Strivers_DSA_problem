def QuickSort(arr,start,end):
    if(start<end):
        pivit = partition(arr,start,end)

        QuickSort(arr,start,pivit-1) # left arr
        QuickSort(arr,pivit+1,end)   # Right arr

def partition(arr,start,end):
    index = start-1  
    pivit = arr[end]

    for j in range(start,end):
        if(arr[j]<pivit):
            index = index+1
            arr[index],arr[j] = arr[j],arr[index]

        
    arr[index+1],arr[end] = arr[end],arr[index+1]        

            

    return index +1

arr = [12,32,54,3,8,43,13,4,5,90]
QuickSort(arr,0,len(arr)-1)
print(arr)