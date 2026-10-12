'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= rows, cols <= 200
matrix[i][j] is '0' or '1'.
'''

# Solution class containing both functions
class Solution:

    # Function to calculate largest rectangle area in histogram
    def largestRectangleArea(self, heights):

        # Add a sentinel bar
        heights.append(0)

        # Stack for indices
        stack = []
        max_area = 0

        # Traverse through histogram bars
        for i in range(len(heights)):

            # Pop and calculate while current is smaller
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            # Push current index
            stack.append(i)

        return max_area

    # Function to find the maximal rectangle in binary matrix
    def maximalRectangle(self, matrix):

        # Return 0 if matrix is empty
        if not matrix: return 0

        # Get column count
        m = len(matrix[0])

        # Initialize histogram
        height = [0] * m
        max_area = 0

        # Traverse each row
        for row in matrix:

            # Update histogram
            for i in range(m):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0

            # Update max area
            max_area = max(max_area, self.largestRectangleArea(height))

        return max_area

object = Solution()
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
print(object.maximalRectangle(matrix))

'''
Time Complexity: O(rows * cols)
Space Complexity: O(cols)
'''
