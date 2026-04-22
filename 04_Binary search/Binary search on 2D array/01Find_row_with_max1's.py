
'''
Example 1:
Input Format: n = 3, m = 3, 
mat[] = 
1 1 1
0 0 1
0 0 0
Result: 0
Explanation: The row with the maximum number of ones is 0 (0 - indexed).


Example 2:
Input Format: n = 2, m = 2 , 
mat[] = 
0 0
0 0
Result: -1
Explanation:  The matrix does not contain any 1. So, -1 is the answer.
'''
# Brute forece approach
class Solution:
    def Find_row(self,nums:list[list[int]]) ->int:
        index = -1
        Max = 0 
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums[0])):
                if nums[i][j] == 1:
                    count += 1
            if count > Max:
                Max = count
                index = i
        return index
nums = [[1,1,1,0],[1,1,1,1],[0,0,0,0],[1,0,0,0]]
object = Solution()
print(object.Find_row(nums))            
'''
Time complexity:O(m*n)
space complexity:O(1)
'''

class Solution:
    def Find_row(self,nums:list[list[int]]) ->int:
        start=0
        end = len(nums[0]) - 1
        index = -1
        while start < len(nums) and end >= 0:
            if nums[start][end] == 1:
                index = start
                end -= 1
            else:
                start += 1
        return index
nums = [[1,1,1,0],[1,1,1,1],[0,0,0,0],[1,0,0,0]]
object = Solution() 
print(object.Find_row(nums))  

'''
Time complexity:O(m+n)
space complexity:O(1)
'''

