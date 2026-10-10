class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        subarray = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                subarray.append(nums[i:j+1])
                if(sum(subarray)%2==0):
                    


    