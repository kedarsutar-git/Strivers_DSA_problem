class Solution:
    def Ifsort(self, nums):
        n = len(nums)

        if n == 0 or n == 1:
            return True

        return nums[n - 2] <= nums[n - 1] and self.Ifsort(nums[:-1])


nums = [1, 2, 3, 4, 5]

obj = Solution()
print(obj.Ifsort(nums))
        