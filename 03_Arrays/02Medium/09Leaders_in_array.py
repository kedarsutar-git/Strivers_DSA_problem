# Brute Force method
class Solution:
    def Leaders_Arr(self,nums:list[int]) -> list[int]:
        temp = []
        for i in range(len(nums)):
            leader = True
            for j in range(i+1,len(nums)):
                if(nums[j]>nums[i]):
                    leader = False
                    break
            if(leader == True):
                temp.append(nums[i])

        return temp            

nums= [10,22,12,3,0,6]
object = Solution()
print(object.Leaders_Arr(nums)) 

'''
Time Complexity :O(n**2)
space Complexity:O(n)
'''

# optimal method
class Solution:
    def Leaders(self,nums:list[int]) -> list[int]:
        Max = 0
        temp = []
        for i in range(len(nums)-1,-1,-1):
            if(nums[i] > Max):
                temp.append(nums[i])

            Max = max(Max,nums[i])

        return temp

nums = [10,22,12,3,0,6]           
object = Solution()
print(object.Leaders(nums))
'''
Time Complexity:O(n)
Sapce Complexity:O(n)
'''


                


