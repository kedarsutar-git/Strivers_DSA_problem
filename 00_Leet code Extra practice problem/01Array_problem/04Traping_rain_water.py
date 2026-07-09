'''
Given n non-negative integers representing an elevation map where the width of each
bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''
class Solution:
    def TrapWater(self,nums:list[int]) ->int:
        start = 0
        end = len(nums)-1
        leftMax ,rightMax = 0,0
        total = 0

        while(start<end):
            leftMax = max(leftMax,nums[start])
            rightMax = max(rightMax,nums[end])

            
            if(leftMax<rightMax):
                total += leftMax - nums[start]
                start+=1

            else:   
                total +=rightMax-nums[end]
                end -=1
        return total      
    
nums =  [4,2,0,3,2,5]
object = Solution()
print(object.TrapWater(nums))

'''
=
Time Complexity:O(n)
Space Complexity:O(1)

'''
