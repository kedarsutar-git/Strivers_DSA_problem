'''
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

'''

class Solution:
    def Subseqarr(self,nums:list[int],index,current,arr):
        if(index==len(nums)):
            arr.append(current)
            return
        

        self.Subseqarr(nums,index+1,current+[nums[index]],arr)
        self.Subseqarr(nums,index+1,current,arr)

object = Solution()

arr = []
object.Subseqarr([1,2,3],0,[],arr)
print(arr)



class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            
            for j in range(len(nums)):
                if(i != j and nums[i] + nums[j] == k):
                    count += 1

        return count
nums = [1, 2, 3, 4, 5]
k = 5
solution = Solution()
result = solution.countSubsequenceWithTargetSum(nums, k)
print(result)  # Output: 2 (subsequences: [1, 4] and [2, 3])


    