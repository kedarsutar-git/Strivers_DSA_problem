'''
Ex:1
Input: M = 3, N = 3, matrix[][] =
1 4 9 
2 5 6
3 8 7
Output: 5
Explanation: 
If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. Therefore, median = 5


Ex:2
Input: M = 3, N = 3, matrix[][] =
1 3 8 
2 3 4
1 2 5
Output: 3
Explanation: 
If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 7 8. Therefore, median = 3.


'''

# Brute Force method
class Solution:
    def Median(self,nums:list[list[int]]) ->int:
        m = len(nums)
        n = len(nums[0])
        temp = []
        for i in range(m):
            for j in range(n):
                temp.append(nums[i][j])
        temp.sort()
        mid =(m*n)//2

        return temp[mid]
nums = [[1,4,9],[2,5,6],[3,8,7]]
object =Solution()
print(object.Median(nums))   
'''
Time Complexity: O(M*N*(log(M*N)))
Space Complexity: O(M*N)
''' 
a = int(input("Enter the number:"))              
b = int(input("Enter the number:"))              
c = int(input("Enter the number:"))
D =  {} 
s = ("kedar","python","Java")
D[a] = s[0]
D[b] = s[1] 
D[c] = s[2]           

