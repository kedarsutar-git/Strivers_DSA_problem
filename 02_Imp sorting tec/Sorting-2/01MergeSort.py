# code 1
def merge_Sort(arr,start,end):
    if(start<end):
        mid = start +(end - start)//2

        merge_Sort(arr,start,mid)
        merge_Sort(arr,mid+1,end)

        merge(arr,start,mid,end)

def merge(arr,start,mid,end):
    temp =[]
    i = start
    j = mid+1
    while(i<=mid and j<=end):
        if(arr[i] <= arr[j]):
            temp.append(arr[i])
            i = i+1

        else:
            temp.append(arr[j])
            j = j+1

    while(i<=mid):
        temp.append(arr[i])
        i = i + 1

    while(j<=end):
        temp.append(arr[j])
        j = j + 1

 # to store element in origenal array
    for index in range(len(temp)):
        arr[index+start] = temp[index]


arr = [12,32,87,43,900,75,46,23] 

merge_Sort(arr,0,len(arr)-1)
print(arr)




# simpler merge sort code of following code 

def merge_sort(arr):
    # Base case: single element is already sorted
    n = len(arr)
    if(n<=1):
        return arr

    mid = len(arr) // 2

    # Divide
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge
    return merge(left, right)


def merge(left, right):
    temp = []
    i = j = 0

    # Compare and merge
    while(i < len(left) and j < len(right)):
        if(left[i] <= right[j]):
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    # Add remaining elements
    temp.extend(left[i:])
    temp.extend(right[j:])

    return temp


arr = [12, 32, 87, 43, 900, 75, 46, 23]
print(merge_sort(arr)) # Function call




# code 2
def merge_sort(arr):
    n = len(arr)
    if(n<=1):
        return arr
    
    mid = n//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return sorted(left+right)

arr = [12,34,645,89,78,76]

print(merge_sort(arr))




'''

| Feature               | Code 1     | Code 2     |
| --------------------- | ---------- | ---------- |
| Uses real merge logic | ✅ Yes     | ❌ No     |
| Time complexity       | O(n log n) | O(n log n) |
| Memory usage          | Less       | More       |
| Best for learning DSA | ✅ Yes     | ❌ No     |

'''

