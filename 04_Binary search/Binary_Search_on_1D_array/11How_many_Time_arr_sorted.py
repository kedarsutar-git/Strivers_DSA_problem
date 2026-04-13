class Solution:
    def Find_Time(self,nums:list[int]) ->int:
        start = 0
        end = len(nums)-1
        ans = 0
        while(start<=end):
            mid = start+(end-start)//2

            if(nums[start]<nums[mid] and nums[mid]<nums[end]):
                ans = nums[start]
                start = mid+1

            elif(nums[mid]<nums[end]):
                ans =  nums[mid]
                end = mid-1
            else:
                end = mid-1
        return ans        
    
nums = [4, 5, 6, 7, 1, 2]
obj = Solution()    
print(obj.Find_Time(nums))
