'''
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2


Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1


Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

'''
class Solution:
    def Search_insert_postion(self,nums:list[int],target) -> int:
        start  = 0
        end = len(nums) -1

        while(start<=end):
            mid = start +(end-start)//2

            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                end = mid-1

            else:
                start = mid+1

        return start
nums  = [1,3,5,6]   
object = Solution()
print(object.Search_insert_postion(nums,7))        

'''
Time Complixity :O(logn)
Space Complixity :O(1)
'''
            

