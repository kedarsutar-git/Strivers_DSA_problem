'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
'''

# Brute force method 

class Solution:
    def kthsmallestnumber(Self,matrix:list[list[int]],k:int)->int:
        List = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                List.append(matrix[i][j])

        List.sort()
        count = 0
        for x in range(len(List)):
            count +=1
            if (count==k):
                ans = List[x]

        return ans 

object = Solution()
matrix = [[1,5,9],[10,11,13],[12,13,15]]
print(object.kthsmallestnumber(matrix,8))

'''
Time Complexity:O(n**2 logn )
Space Complexity:O(n**2)

'''

# optimal method 
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        left  = matrix[0][0]  # smallest number in the matrix 
        right = matrix[len(matrix)-1][len(matrix)-1] # largest number in the matrix 

        while(left<right):
            mid = left + (right-left)//2

            count = 0
            row = len(matrix)-1
            col = 0
            while(row>=0 and col<len(matrix)):
                if(matrix[row][col]<=mid):
                    count += row + 1
                    col += 1
                
                else:
                    row -= 1

            if(count<k):
                left = mid + 1
            
            else:
                right = mid
        
        return left 

matrix =[[1,5,9],[10,11,13],[12,13,15]]

object = Solution()
print(object.kthSmallest(matrix,8))

'''
Time Complexity:O(nlogR)
Space Complexity:O(1)
'''