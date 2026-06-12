class Solution:
    def RemoveDup(self,nums:list[int]) ->list[int]:
        s = set()
        for i in range(len(nums)):
            s.add(nums[i])
            L = list(set(s))
        return L
    
nums = [1,2,3,3,4,5,6] 
object = Solution()
print(object.RemoveDup(nums))  

'''
Time ComplexityO(n)
Space Complexity(n)
'''



        