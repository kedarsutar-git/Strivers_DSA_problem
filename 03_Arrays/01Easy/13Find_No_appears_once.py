
def find(arr):
    n = len(arr)
    for i in range(n+1):
        if(arr[i-1]!=arr[i]!=arr[i+1]):
            return arr[i]
        return -1
arr = [1,1,2,2,3,4,4,5,5]
print(find(arr))
'''Time complexity:O(n)
    Space Complexity:O(1)
'''


def Find(arr):
    n = len(arr)
    
    if n == 1:
        return arr[0]
    
    start = 0
    end = n - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        # If single element found
        if mid > 0 and mid < n-1 and arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        
        # Handle first element
        if mid == 0:
            return arr[0] if arr[0] != arr[1] else None
        
        # Handle last element
        if mid == n-1:
            return arr[n-1] if arr[n-1] != arr[n-2] else None
        
        # If mid is even
        if mid % 2 == 0:
            if arr[mid] == arr[mid+1]:
                start = mid + 2
            else:
                end = mid - 1
        
        # If mid is odd
        else:
            if arr[mid] == arr[mid-1]:
                start = mid + 1
            else:
                end = mid - 1

arr = [1,1,2,2,3,4,4,5,5]
print(Find(arr))
'''
Time complixity:O(log(n))
Space complixity:O(1)

'''

