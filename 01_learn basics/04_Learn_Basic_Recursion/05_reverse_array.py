class solution:
    def reverseArr(self,nums:list[int]) ->list[int]:
        start,end = 0,len(nums)-1
        while(start < end):
            nums[start],nums[end] = nums[end],nums[start]
            start +=1
            end-=1

        return nums
nums = [1,2,3,4,5,6] 
object = solution()
print(object.reverseArr(nums))

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''


