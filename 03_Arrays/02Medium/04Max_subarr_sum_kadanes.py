# optimal method(kadanes algorithm)
def max_subarray_sum(arr):
    n = len(arr)
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1,n):
        current_sum = max(arr[i],arr[0]+arr[i])
        max_sum = max(max_sum,current_sum)

    return max_sum

arr = [1,2,5,3,2,4,6,4,3,5,3]
print(max_subarray_sum(arr))

'''
Time complixity:O(n)
space complixity:O(1)
'''


# leet code Style 
class Solution:
    def Max_SubArr_Sum(self,nums:list[int]) -> int:
        Max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i],nums[0]+nums[i])
            Max_sum = max(Max_sum,current_sum)

        return Max_sum

nums =  [1,2,5,3,2,4,6,4,3,5,3]  
object = Solution()
print(object.Max_SubArr_Sum(nums))
     
            