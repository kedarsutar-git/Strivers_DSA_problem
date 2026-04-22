class Solution:
    def BinarySearch(self,nums:list[int],target:int) -> int:
        start = 0
        end = len(nums)- 1

        while(start<=end):
            mid = start + (end-start)//2

            if(nums[mid]==target):
                return mid
            
            elif(nums[mid]< target):
                start = mid +1

            elif(nums[mid]>target):
                end = mid -1

        return -1

nums = [1,2,4,6,7,8]
object = Solution()
print(object.BinarySearch(nums,8))                

'''
Time Complexity:O(logn)
Space Complexity :O(1)
'''

