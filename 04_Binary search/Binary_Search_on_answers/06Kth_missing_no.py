# Brute Force Approach
class Solution:
    def Kth_missing(self,nums:list[int],k:int) ->int:
        temp1 = []
        temp2 = []
        for i in range(1,max(nums)):
            temp1.append(i)

        for i in temp1:
            if i not in nums:
                temp2.append(i) 
        return temp2[k-1] 

nums = [2,3,4,7,11]
object =Solution()
print(object.Kth_missing(nums,5))
'''
Time Complixity:O(n**2)
Space Complixity:O(n)

'''


