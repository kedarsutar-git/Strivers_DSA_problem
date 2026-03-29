'''
majority element >n//3
n = len(arr)

'''
class Solution:
    def Majority(self,nums:list[int]) ->list[int]:
        temp = []
        n = len(nums)
        for i in range(len(nums)):
            count = 1
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    count +=1

            if(count>n//3 and nums[i] not in temp):
                temp.append(nums[i])

        return temp

nums = [1,1,1,2,2,3,3,3]
object = Solution()
print(object.Majority(nums))            
                    