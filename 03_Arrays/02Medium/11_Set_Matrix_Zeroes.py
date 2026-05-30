'''
Input: matrix=[[1,1,1],
               [1,0,1],
               [1,1,1]]
Output: [[1,0,1],
         [0,0,0],
         [1,0,1]]
Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

Input: matrix=[[0,1,2,0],
               [3,4,5,2],
               [1,3,1,5]]
Output:[[0,0,0,0],
        [0,4,5,0],
        [0,3,1,0]]
Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0
'''



# Brute force method

class Solution:
    def SetMatrix(self, nums: list[list[int]]) -> list[list[int]]:
        rows = len(nums)
        cols = len(nums[0])

        zero_rows = set()
        zero_cols = set()

        # Step 1: Record all positions where 0 exists
        for i in range(rows):
            for j in range(cols):
                if nums[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Step 2: Mark entire row as 0
        for i in zero_rows:
            for j in range(cols):
                nums[i][j] = 0

        # Step 3: Mark entire col as 0
        for j in zero_cols:
            for i in range(rows):
                nums[i][j] = 0

        return nums

nums = [[1,1,1,1],
        [1,0,0,1],
        [1,1,0,1],
        [1,1,1,1]]

obj = Solution()
print(obj.SetMatrix(nums))

'''
Time Complexity:O(n**3)
space Complexity :O(n**2)
'''


# Better method
class Solution:
    def SetMatrix(self,nums:list[list[int]]) -> list[list[int]]:
        row = len(nums)
        col = len(nums[0])
        rows = [0]*row
        cols = [0]*col
        for i in range(row):
            for j in range(col):
                if(nums[i][j]==0):
                    rows[i] = 1
                    cols[j] = 1

        for i in range(row):
            for j in range(col):
                if(rows[i]==1 or cols[j]==1):
                    nums[i][j]=0
        return nums            
nums = [[1,1,1,1],
        [1,0,0,1],
        [1,1,0,1],
        [1,1,0,1]] 
object = Solution()
print(object.SetMatrix(nums))

'''
Time Complexity:O(2 X row X col)
space complexith :O(rows) +O(cols)
'''


class Solution:
    def SetMatrixZeros(self,nums:list[list[int]]) -> list[list[int]]:
        row = len(nums)
        col = len(nums[0])
        rows = [0]*len(nums)
        cols = [0]*len(nums[0])

        for i in range(row):
            for j in range(col):
                if(nums[i][j]==0):
                    rows[i]=1
                    cols[j]=1

        for i in range(row):
            for j in range(col):
                if(rows[i]==1 or cols[j]==1):
                    nums[i][j]=0

        return nums                        
nums = [[1,1,1,1],
        [1,0,0,1],
        [1,1,0,1],
        [1,1,0,1]] 
object = Solution()
print(object.SetMatrixZeros(nums))
       