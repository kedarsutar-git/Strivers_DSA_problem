# Brute force method 
def TwoSum(arr):
    n = len(arr)
    tar = 10
    for i in range(n):
        for j in range(i+1,n):
            arr[i]+arr[j]
            if(arr[i]+arr[j]==tar):
                return 1

            else:
                return 0
arr = [1,2,3,4,5,6]
print(TwoSum(arr))    
   
'''
Time Complixity: O(n**2)
space Complixity:O(1)

'''   
# optimal method
class Solution:
    def TwoSum(self,nums:list[int])-> int:
        tar = 10
        D = {}
        for i in range(len(nums)): # O(n)
            first = nums[i]
            sec = tar - first
            if sec in D:
                return [D[sec],i] # O(1)

            D[first] = i
nums = [1,2,3,4,5,6]
object = Solution()
print(object.TwoSum(nums))
'''
Time Complixity:O(n)
Space Complixity:O(n)
'''

# leet code Style 
class Solution:
    def Twosum(self,nums:list[int],tar:int) -> int:
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(nums[i]+nums[j]==tar):
                    return 1
                return -1
nums = [1,2,3,4,5,6]
object  = Solution()
print(object.Twosum(nums,10))

