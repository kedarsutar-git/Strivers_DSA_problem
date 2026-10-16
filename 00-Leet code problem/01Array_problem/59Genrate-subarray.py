
# Method - 1

class Solution:
    def genratesubarray(self,nums:list[int]):
        ans = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                subarray = []
                for k in range(i,j+1):
                    subarray.append(nums[k])

                ans.append(subarray)

        return ans 

object = Solution()
nums = [1,2,3]
print(object.genratesubarray(nums))


# Method - 2

class Solution:
    def GenrateSubarray(self,nums:list[int]):
        all_subarray = []
        for i in range(len(nums)):
            current_subarr = []
            for j in range(i,len(nums)):
                current_subarr.append(nums[j])

                all_subarray.append(list(current_subarr))   # list is the copy of current_subarr

        return all_subarray

object = Solution()
nums = [1,2,3]
print(object.GenrateSubarray(nums))

# Method - 3

class Solution:
    def GenSubarray(self,nums:list[int]):
        sub_arr = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                sub_arr.append(nums[i:j])

        return sub_arr
object = Solution()
nums = [1,2,3]
print(object.GenSubarray(nums))



