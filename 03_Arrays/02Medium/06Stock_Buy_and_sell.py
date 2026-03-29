# Optimal method:
class Solution:
    def Stock(self,nums:list[int]) -> int:
        MaxProfit = 0
        BestBuy = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]>BestBuy):
                MaxProfit = max(MaxProfit,nums[i])

            BestBuy = min(BestBuy,nums[i])

        return MaxProfit

nums = [7,1,5,3,6,4]
object = Solution()
print(object.Stock(nums))            

'''
Time complixity:O(n)
Space Complixity:O(1)
'''