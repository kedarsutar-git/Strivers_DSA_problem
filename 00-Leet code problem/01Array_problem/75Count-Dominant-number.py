'''
You are given an integer array nums.

An element in nums is called dominant if it is greater than or equal to the average of its immediate neighbors.

The immediate neighbors of nums[i] are nums[i - 1] and nums[i + 1], when those indices exist.

A single element with no neighbors is considered dominant.

Return the number of dominant elements in nums.

 

Example 1:

Input: nums = [1,10,2]

Output: 1

Explanation:

For nums[0] = 1, its only neighbor is 10. Since 1 < 10, it is not dominant.
For nums[1] = 10, its neighbors are 1 and 2. Their average is (1 + 2) / 2 = 1.5. Since 10 > 1.5, it is dominant.
For nums[2] = 2, its only neighbor is 10. Since 2 < 10, it is not dominant.
Therefore, the answer is 1.

Example 2:

Input: nums = [6,4,2]

Output: 2

Explanation:

For nums[0] = 6, its only neighbor is 4. Since 6 > 4, it is dominant.
For nums[1] = 4, its neighbors are 6 and 2. Their average is (6 + 2) / 2 = 4. Since 4 = 4, it is dominant.
For nums[2] = 2, its only neighbor is 4. Since 2 < 4, it is not dominant.
Therefore, the answer is 2.

Example 3:

Input: nums = [7]

Output: 1

Explanation:

For nums[0] = 7, it has no neighbors, so it is dominant.
Therefore, the answer is 1.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''

class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 1
        count = 0 
        for i in range(len(nums)):
            if i==0:
                if nums[i]>=nums[i+1]:
                    count += 1

            elif i==len(nums)-1:
                if nums[i]>=nums[i-1]:
                    count += 1

            else:
                if nums[i]*2>=(nums[i+1]+nums[i-1]):
                    count += 1

        return count 

nums = [6,4,2]
object = Solution()
print(object.countDominantElements(nums))
'''
Time Complexity:O(n)
Space Complexity:O(1)
'''

