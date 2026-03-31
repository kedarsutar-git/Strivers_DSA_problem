'''
find the missing number 
'''
class Solution:
    def missNo(self,nums:list[int]) -> list[int]:
        temp = []
        n = len(nums)
        Tsum = (n+1)*(n+2)//2
        Esum = sum(nums)

        Sum = Tsum-Esum
        temp.append(Sum)
        
        return temp
nums = [1,2,3,4,6,7]
object = Solution()
print(object.missNo(nums))


'''
Find Repeting Number
'''
class Solution:
    def FindNo(self,nums:list[int]) -> list[int]:
        s = set()
        nums.sort()
        
        for i in range(1,len(nums)-1):
            if(nums[i-1]==nums[i] or nums[i]==nums[i+1]):
                s.add(nums[i])
                l = list(set(s))

        return l     
nums = [1,2,3,4,5,5,6,7,8]
object = Solution()
print(object.FindNo(nums)) 






