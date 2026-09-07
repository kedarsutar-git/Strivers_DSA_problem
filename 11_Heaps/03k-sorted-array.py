class Solution:
    def ksortedArray(self, nums:list[int], k:int) ->list[int]:
        heap = []
        ans= [] 
        for i in range(len(nums)):
            heap.append(nums[i])

            heap.sort()
            heap.reverse()

            if(len(heap)>k):
                ans.append(heap.pop())

        while(len(heap)!=0):
            ans.append(heap.pop())

        return ans 

object = Solution()
nums = [6,5,3,2,8,10,9]
print(object.ksortedArray(nums,3))

'''
Time Complexity:O(nklonk)
space Complexity:O(n)
'''







