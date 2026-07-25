'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

class Solution:
    def maxlenOnes(self,nums:list[int]) ->int:
        left,right = 0,0
        maxlen = 0
        zeros = 0
        while(right<len(nums)):
            if(nums[right]==0):
                zeros += 1

            while(zeros>1):
                if(nums[left]==0):
                    zeros -=1
                left += 1

                length = right -left
                maxlen = max(maxlen,length)

            right +=1

        return maxlen

nums = [0,1,1,1,0,1,1,0,1]
object = Solution()
print(object.maxlenOnes(nums))

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''