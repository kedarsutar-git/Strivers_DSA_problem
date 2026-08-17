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
Time Complexity:O(logn+n^2+n)
Space Complexity:O(n)

'''
