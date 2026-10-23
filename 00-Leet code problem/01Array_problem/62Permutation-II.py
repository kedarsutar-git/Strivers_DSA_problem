'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''

class Solution:
    def genper(self, nums, index, ans):
        if index == len(nums):
            ans.append(nums[:])
            return

        used = set()  # Avoid duplicate values at this position

        for i in range(index, len(nums)):
            if nums[i] in used:
                continue

            used.add(nums[i])

            nums[index], nums[i] = nums[i], nums[index]
            self.genper(nums, index + 1, ans)
            nums[index], nums[i] = nums[i], nums[index]

    def permuteUnique(self, nums):
        ans = []
        self.genper(nums, 0, ans)
        return ans


nums = [1, 1, 2]
obj = Solution()
print(obj.permuteUnique(nums))

'''
Time Complexity:O(n!*n)
Space Complexity:O(n)

'''