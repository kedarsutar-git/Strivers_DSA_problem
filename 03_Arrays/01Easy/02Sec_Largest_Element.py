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


# leet code style 
class Solution:
    def Seclar(self,nums:list[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if(nums[j]>nums[j+1]):
                    nums[j],nums[j+1] = nums[j+1],nums[j]

        return nums[len(nums)-2]  
nums = [12,23,345,6,56,77,68,6,8454]
object = Solution()
print(object.Seclar(nums))              

