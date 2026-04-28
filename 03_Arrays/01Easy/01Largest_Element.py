# Brute Force method 
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
            
'''
Time Complexity:(n)
Sapce Complexity:(1)
'''            

class Solution:
    def Largest(self,arr:list[int]) -> int:
        for i in range(len(arr)):
            for j in range(1,len(arr)-1):
                if(arr[i]>arr[j]):
                    arr[i],arr[j] = arr[j],arr[i]

                    return arr
        return arr[len(arr)-1]

arr = [9,87,6,54,3,2,1 ]            


