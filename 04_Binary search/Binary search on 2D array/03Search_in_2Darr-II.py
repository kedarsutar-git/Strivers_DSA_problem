'''
Example 1:
Input: matrix = [[1,4,7,11,15],
                 [2,5,8,12,19],
                 [3,6,9,16,22],
                 [10,13,14,17,24],
                 [18,21,23,26,30]], target = 5
Output: true


Example 2:
Input: matrix = [[1,4,7,11,15],
                 [2,5,8,12,19],
                 [3,6,9,16,22],
                 [10,13,14,17,24],
                 [18,21,23,26,30]], target = 20
Output: false  
'''

# Brute Force method
class Solution:
    def search2DMatrix(self, Matrix: list[list[int]], target: int) -> bool:
        for i in range(len(Matrix)):
            for j in range(len(Matrix[0])):
                if (Matrix[i][j] == target):
                    return True
        return False    
    
Matrix = [[3,4,7,9],[12,13,16,18],[20,21,23,29]] 
object = Solution() 
print(object.search2DMatrix(Matrix,20))            
'''
Time Complixity:(n*m)
space Complixity:O(1)
'''  

# Optimal method
class Solution: 
    def SearchIn2Darr(self,Matrix:list[list[int]],target:int) ->bool:
        m = len(Matrix)
        n = len(Matrix[0])
        r = 0
        c = n-1
        while(c>=0 and r<m):
            if(target==Matrix[r][c]):
                return True
            
            elif(Matrix[r][c]>target):
                c-=1

            elif(Matrix[r][c]<target):
                r+=1

        return False
Matrix = [[3,4,7,9],[12,13,16,18],[20,21,23,29]]
object = Solution()
print(object.SearchIn2Darr(Matrix,20))     
'''
Time Complixity:O(m+n)
space Complixity:O(1)
'''

