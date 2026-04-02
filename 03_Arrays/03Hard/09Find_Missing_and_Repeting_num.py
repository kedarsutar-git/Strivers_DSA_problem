class Solution:
    def FindMissingandRepeting(self, nums: list[int]) -> None:
        nums.sort()

        repeating = None
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                repeating = nums[i]
                break

        unique_nums = set(nums)

        n = len(nums)
        total_sum = n * (n + 1) // 2         
        actual_sum = sum(unique_nums)
        missing = total_sum - actual_sum

        print(f"The Missing number is : {missing}")
        print(f"The Repeating number is : {repeating}")


nums = [1, 3, 4, 4, 5, 6, 7, 8]
obj = Solution()
obj.FindMissingandRepeting(nums)