class Solution:
    def Maxconsecutive(self,nums:list[int]) -> int:
        count = 0 
        Max = 0
        for n in nums:
            if(n==1):
                count +=1
                Max = max(Max,count)

            else:
                count = 0

        return Max
nums = [1,0,0,0,1,1,1,0,0,0,1,1,1,1] 
object = Solution()
print(object.Maxconsecutive(nums))  
'''
Time complexity: O(n)
Space complexity: O(1)
'''

            

