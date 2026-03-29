# Brute Force method 
class Solution:
    def SunArr(self,nums:list[int],k:int) -> int:
        count = 0 
        for i in range(len(nums)):
            sum = 0 
            for j in range(i,len(nums)):
                sum +=nums[j]
                if(sum==k):
                    count +=1

        return count

nums = [1,2,3,4,5,6,7,8,134]
object = Solution()
print(object.SunArr(nums,9))                

'''
Time Complixity :O(n**2)
Space Complixity :O(1)
'''

# optimal method
class Solution:
    def subarr(self,nums:list[int],k:int) -> int:
        count = 0
        D = {}
        ps = [0] * len(nums)

        ps[0] = nums[0]              
        for i in range(1, len(nums)):
            ps[i] = ps[i-1] + nums[i]

        for j in range(len(nums)):
            if ps[j] == k:
             count += 1
        val = ps[j] - k
        if val in D:
            count += D[val]
        D[ps[j]] = D.get(ps[j], 0) + 1   

        return count

arr = [9, 4, 20, 3, 10, 5]
object = Solution()
print(object.subarr(arr,33)) 
