'''
Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

 

Example 1:


Input: m = 3, n = 3, k = 5

Matrix:

1  2  3
2  4  6
3  6  9

Sorted elements:

1  2  2  3  3  4  6  6  9

Input:
m = 3, n = 3, k = 5

Output: 3
Explanation: The 5th smallest number is 3.



Example 2:

Matrix:

1  2  3
2  4  6

Sorted elements:

1  2  2  3  4  6

Input:
m = 2, n = 3, k = 6
Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.
 

Constraints:

1 <= m, n <= 3 * 104
1 <= k <= m * n
'''
# Brute force method 

class Solution:
    def KthSmallestnumber(self,m:int,n:int,k:int) ->int:
        matrix = []
        for i in range(1,n+1):
            row = []
            for j in range(1,m+1):
                row.append(i*j)

            matrix.append(row)


        arr =[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr.append(matrix[i][j])

        arr.sort()

        count = 0
        for x in range(len(arr)):
            count += 1
            if(count==k):
                ans = arr[x]

        return ans

object = Solution()
print(object.KthSmallestnumber(3,3,5))

'''
Time Complexity : O(nm log(nm))	
Space Complexity: O(nm)
'''

# optimal method 
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        start = 0
        end = m*n

        while(start<end):
            mid = start + (end - start)//2

            count = 0
            for i in range(1,n+1):
                count += min(m,mid//i)

            if(count<k):
                start = mid+1
            else:
                end = mid
        
        return start


object = Solution()
print(object.findKthNumber(3,3,5))