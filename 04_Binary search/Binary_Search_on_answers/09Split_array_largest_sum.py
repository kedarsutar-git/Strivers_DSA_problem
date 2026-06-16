

'''
Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum
among the two subarrays is only 18.



Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest 
sum among the two subarrays is only 9.
'''

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        if(k>len(nums)):
            return -1

        start = max(nums)
        end = sum(nums)

        while(start<=end):
            mid = start +(end-start)//2
            Sum = 0
            split = 1
            for num in nums:
                if(Sum+num<=mid):
                    Sum +=num
                else:
                    split +=1
                    Sum = num
                    
            if(split>k):
                start = mid+1

            else:
                end = mid-1

        return start                            
        
nums =  [10, 20, 30, 40]
object = Solution()
print(object.splitArray(nums, 2)) 
'''
Time Complexity:O(nlogn)
Space Complexity:O(1)

'''