class Solution:
    def dignalSum(self,matrix:list[list[int]]) ->int:
        primarydignalSum = 0
        secdigonalSum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i==j):
                    primarydignalSum +=matrix[i][j]

                if(i+j==len(matrix)-1 and i!=j):
                    secdigonalSum += matrix[i][j]

        return primarydignalSum+secdigonalSum

object = Solution()
matrix= [[1,2,3],
              [4,5,6],
              [7,8,9]]
print(object.dignalSum(matrix))    

'''
Time Complexity:O(n^2)
Space Complexity:O(1)

'''