class Solution:
    def SubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Sum of first window
        currentSum = sum(nums[:k])
        Max = currentSum

        # Slide the window
        for i in range(k, n):
            currentSum = currentSum + nums[i] - nums[i-k]
            Max = max(Max, currentSum)

        return Max


obj = Solution()
nums = [2, 3, 5, 2, 9, 7, 1]
print(obj.SubarraySum(nums, 3))

'''
Time Complexity :O(n)
space Complexity:O(1)

'''