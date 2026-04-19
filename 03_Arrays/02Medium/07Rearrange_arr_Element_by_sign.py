# Brute force method
class Solution:
    def Rearrange(self,nums:list[int]) -> list[int]:
        positive = []
        negative = []
        n = len(nums)//2
        for num in nums: # O(n)
            if(num>0):
                positive.append(num)

            else:
                negative.append(num)

        for i in range(n):  # O(n/2)
            nums[2*i] = positive[i]
            nums[2*i+1] = negative[i]

        return nums

nums= [3,1,-2,-5,2,-4] 
object = Solution()
print(object.Rearrange(nums))
'''
Time Complexity:O(n) +O(n/2)
Space complexity: O(n/2)+O(n/2) = O(n)
 '''

# optimal method
class Solution:
    def rearrange(self,nums:list[int]) -> list[int]:
        ans = [0] * len(nums)
        posIndex = 0
        negIndex = 1
        for i in range(len(nums)):
            if(nums[i] < 0):
                ans[negIndex] = nums[i]
                negIndex +=2
            else:
                ans[posIndex] = nums[i]
                posIndex +=2

        return ans

nums = [3,1,-2,-5,2,-4]  
object = Solution()
print(object.rearrange(nums))        
'''
Time complexity : O(n)
Space Complexity: O(n)

'''



# Note:

'''
ans = [0] * len(nums) — Pre-filled List

 1.Creates a list with n slots, all filled with 0 as placeholders
 2.Has valid indices from 0 to n-1
 3.You can directly assign to any index




nums = [3, 1, -2, -5, 2, -4]  # len = 6
ans = [0] * len(nums)
print(ans)   # [0, 0, 0, 0, 0, 0]

ans[0] = 5   # ✅ Works fine
print(ans)   # [5, 0, 0, 0, 0, 0]
                
'''




