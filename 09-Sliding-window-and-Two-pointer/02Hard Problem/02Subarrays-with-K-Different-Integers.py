'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]


Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
'''
# Brute force method 

class Solution:
    def countsubarr(self,nums:list[int],k:int) ->int:
        count = 0
        for i in range(len(nums)):
            count_map = {}
            for j in range(i,len(nums)):
                if nums[j] in count_map:
                    count_map[nums[j]] += 1

                else:
                    count_map[nums[j]] = 1

                while(len(count_map)>k):
                    break

                if(len(count_map)==k):
                    count +=1

        return count

nums = [1,2,1,3,4]
object = Solution()
print(object.countsubarr(nums,3))       
'''
Time Complexity:O(n**2)
Space Complexity:O(n)

'''

class Solution:
    def Atmost(self,nums:list[int],k:int) ->int:
        count = 0
        right, left = 0, 0
        count_map = {}
        while(right<len(nums)):
            if nums[right] in count_map:
                count_map[nums[right]] += 1

            else:
                count_map[nums[right]] = 1

            while(len(count_map)>k):

                count_map[nums[left]] -=1

                if(count_map[nums[left]]==0):
                    del count_map[nums[left]]

                left += 1

            count += (right -left +1)

            right += 1

        return count 
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:

        return self.Atmost(nums,k) - self.Atmost(nums,k-1)   #  Exactly(K) = AtMost(K)-AtMost(K-1)
                            
        
nums = [1,2,1,3,4]
object = Solution()
print(object.subarraysWithKDistinct(nums,3))

'''
Time complexity:O(n)
Space complexity:O(n)

'''

'''
               Exactly K

               AtMost(K)
        ┌─────────────────────┐
        │                     │
        │ 1 distinct          │
        │ 2 distinct          │
        │ 3 distinct          │
        │                     │
        └─────────────────────┘

                  Minus

             AtMost(K-1)

        ┌─────────────────┐
        │1 distinct       │
        │2 distinct       │
        └─────────────────┘

                 Equals

        ┌─────────────────┐
        │3 distinct only  │
        └─────────────────┘
'''

