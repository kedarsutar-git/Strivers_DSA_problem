'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.



Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).



Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
'''

class Solution:
    def KDiffPairs(Self,nums:list[int],k:int) ->int:
        s = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(abs(nums[i]-nums[j])==k):
                    s.add(tuple(sorted((nums[i],nums[j]))))

        return len(s)

nums = [1,2,3,4,5]
object =Solution()
print(object.KDiffPairs(nums,1))

'''
Time Complexity:O(n^2)
Space Complexity:O(n)
'''

class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        if(k < 0):
            return 0

        nums.sort()

        left = 0
        right = 1
        count = 0

        while(right < len(nums)):

            if(left == right):
                right += 1
                continue

            diff = nums[right] - nums[left]

            if(diff < k):
                right += 1

            elif(diff > k):
                left += 1

            else:
                count += 1

                left_val = nums[left]
                right_val = nums[right]

                while(left < len(nums) and nums[left] == left_val):
                    left += 1

                while(right < len(nums) and nums[right] == right_val):
                    right += 1

        return count
    
nums = [1,2,3,4,5]
object =Solution()
print(object.findPairs(nums,1))  

'''
Time Complexity:O(nlogn)
Space Complexity:O(1)
'''