def largest(arr):
    n = len(arr)
    largest = arr[0]
    for i in range(1,n):
        if(arr[i]>largest):
            largest = arr[i]

    return largest
arr = [12,34,56,4,3,56,778,55]
print(largest(arr))      

# leetcode style 
class Solution:
    def Largest(self,nums:list[int]) -> int:
        largest = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]>largest):
                largest = nums[i]

        return largest
nums = [12,23,45,56,67,78,7823] 
obj = Solution()
print(obj.Largest(nums))   
            


