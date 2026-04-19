class soultion:
    def Find(self,nums:list[int]) -> int:
        for i in range(1,len(nums)):
            if(nums[i-1]!=nums[i]!=nums[i+1]):
                return nums[i]
        return -1
nums = [1,1,2,2,3,3,4,5,5,6,6]
object = soultion()
print(object.Find(nums))
'''Time complexity:O(n)
    Space Complexity:O(1)
'''


class Solution:
    def Find(self,arr:list[int]) -> int :
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
object =Solution()
print(object.Find(arr))
'''
Time complexity:O(log(n))
Space complexity:O(1)

'''





