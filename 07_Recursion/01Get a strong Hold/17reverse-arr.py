class Solution:
    def revarr(self,nums:list[int],start,end):
        if(start==end):
            return nums

        if(start<=end):
            nums[start],nums[end] = nums[end],nums[start] 

        return self.revarr(nums,start+1,end-1)
    
object = Solution()
nums = [1,2,3,4,5]
print(object.revarr(nums,0,len(nums)-1))   