'''
Ex:1
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Ex:2
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''
# Brute forece approach
class Solution:
    def SearchMatrix(self,Matrix:list[list[int]],target:int) ->bool:
        for i in range(len(Matrix)):
            for j in range(len(Matrix)):
                if(Matrix[i][j]==target):
                    return True
        return False
Matrix = [[3,4,7,9],[12,13,16,18],[20,21,23,29]]
object = Solution()
print(object.SearchMatrix(Matrix,20))            
'''
Time Complixity:(n*m)
space Complixity:O(1)
'''

# Optimal method
class Solution:
    def searchInRow(self, Matrix, target, midRow):
        n = len(Matrix[0])
        start = 0
        end = n - 1

        while start <= end:
            mid = start + (end - start) // 2

            if Matrix[midRow][mid] == target:
                return True

            elif target > Matrix[midRow][mid]:
                start = mid + 1
            else:
                end = mid - 1

        return False

    def search2DMatrix(self, Matrix: list[list[int]], target: int) -> bool:
        m = len(Matrix)
        n = len(Matrix[0])

        startRow = 0
        endRow = m - 1

        while startRow <= endRow:
            midRow = startRow + (endRow - startRow) // 2

            if target >= Matrix[midRow][0] and target <= Matrix[midRow][n - 1]:
                return self.searchInRow(Matrix, target, midRow)

            elif target > Matrix[midRow][n - 1]:
                startRow = midRow + 1
            else:
                endRow = midRow - 1

        return False


Matrix = [[3,4,7,9],[12,13,16,18],[20,21,23,29]]
obj = Solution()
print(obj.search2DMatrix(Matrix, 99))   

'''
Time Complixity:O(log(n*m))
Sapce Complixity:O(1)

'''




    
