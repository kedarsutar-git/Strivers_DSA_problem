'''
Example 1:
Input:
mat = [[5, 10, 8],
       [4, 25, 7], 
       [3, 9,  6]]
Output:
[1, 1]
Explanation:
The value at index [1, 1] is 25, which is a peak because all its neighbors (10, 7, 4, 9) are smaller.

Example 2:
Input:
mat = [[1, 2, 3], 
       [6, 5, 4], 
       [7, 8, 9]]
Output:
[2, 2]
Explanation:
 The value at index [2, 2] is 9, which is a peak as it is greater than its neighbors (8, 4).
'''

# Brute Force method(find largest element in the Matrix)               
class Solution:
    def FindPeak(self,nums:list[list[int]]) ->int:
        m = len(nums)
        n = len(nums[0])
        Max = nums[0][0]
        Max_row,Max_col = 0,0
        for i in range(m):
            for j in range(n):
                if(nums[i][j]>Max):
                    Max = max(nums[i][j],Max)
                    Max_row,Max_col = i,j
        return [Max_row,Max_col]           
                      
nums = [[5, 1000, 8],[4, 256, 7],[3, 900,  60]]
object =Solution()
print(object.FindPeak(nums)) 
'''
Time Complixity:O(n**2)
Space Complixity:O(1)

'''
