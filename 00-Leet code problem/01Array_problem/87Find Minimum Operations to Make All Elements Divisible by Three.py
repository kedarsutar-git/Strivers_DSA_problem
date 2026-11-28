'''
You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

Return the minimum number of operations to make all elements of nums divisible by 3.

 

Example 1:

Input: nums = [1,2,3,4]

Output: 3

Explanation:

All array elements can be made divisible by 3 using 3 operations:

Subtract 1 from 1.
Add 1 to 2.
Subtract 1 from 4.
Example 2:

Input: nums = [3,6,9]

Output: 0

 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
'''

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
             if nums[i]%3 != 0:
                count += 1

        return count 

nums = [1,2,3,4]
object = Solution()
print(object.minimumOperations(nums))


'''
Time Complexity:O(n)
Space Complexity:O(1)

'''