# Brute Force method
class solution:
    def Check(self,nums:list[int]) -> bool:
        for i in range(1,len(nums)):
            if(nums[i]<nums[i-1]):
                return False
        
        return True    
               
        
nums = [12,13,14,15,16,17,18,19,2] 
object = solution()
print(object.Check(nums))
'''
Time Complexity:O(n)
Space Complexity:O(1)
'''
