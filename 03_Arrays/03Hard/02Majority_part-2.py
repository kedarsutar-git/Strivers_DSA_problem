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
                    

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        candidate1 = None
        candidate2 = None

        count1 = 0
        count2 = 0

        # Step 1: Find potential candidates
        for num in nums:

            if candidate1 == num:
                count1 += 1

            elif candidate2 == num:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates
        result = []

        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)

        if candidate2 != candidate1 and nums.count(candidate2) > len(nums) // 3:
            result.append(candidate2)

        return result


nums = [1,1,1,2,2,3,3,3]
obj = Solution()
print(obj.majorityElement(nums))

                  


            
                                                            