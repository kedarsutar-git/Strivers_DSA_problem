def Maxcount(arr):
    count = 0
    Max = 0
    for num in arr:
        if(num==1):
            count = count+1
            Max = max(Max,count)

        else:
            count = 0

    return Max

arr = [1,0,0,0,1,1,1,0,0,0,1,1,1,1]
print(Maxcount(arr))
'''
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def Maxconsecutive(self,nums:list[int]) -> int:
        count = 0 
        Max = 0
        for n in nums:
            if(n==1):
                count +=1
                Max = max(Max,count)

            else:
                count = 0

        return Max
nums = [1,0,0,0,1,1,1,0,0,0,1,1,1,1] 
object = Solution()
print(object.Maxconsecutive(nums))              

