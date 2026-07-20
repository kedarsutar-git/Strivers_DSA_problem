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
