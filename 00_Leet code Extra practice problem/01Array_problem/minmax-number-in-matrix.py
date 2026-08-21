class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        minrow = []
        maxcol = []

        for i in range(len(matrix)):
            minnum = matrix[i][0]

            for j in range(len(matrix[0])):
                if(matrix[i][j]<minnum):
                    minnum = matrix[i][j]

                minrow.append(minnum)

        for i in range(len(matrix[0])):
            maxnum = matrix[i][j]

            for j in range(len(matrix)):
                if(matrix[i][j]>maxnum):
                    maxnum = matrix[i][j]

                maxcol.append(maxnum)
        return maxcol ,minrow

object = Solution()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(object.luckyNumbers(matrix))