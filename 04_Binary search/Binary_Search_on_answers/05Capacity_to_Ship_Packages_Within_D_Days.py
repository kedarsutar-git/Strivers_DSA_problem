class Solution:
    def Least_capacity(self,nums:list[int],days:int) -> int:
        start = max(nums)
        end = sum(nums)
        while start <= end:
            mid = (start + end) // 2
            days_needed = 1
            current_load = 0
            for weight in nums:
                if current_load + weight > mid:
                    days_needed += 1
                    current_load = weight
                else:
                    current_load += weight
            if days_needed <= days:
                end = mid - 1
            else:
                start = mid + 1
        return start    
nums = [1,2,3,4,5,6,7,8,9,10]
  
object = Solution()

print(object.Least_capacity(nums,5))
