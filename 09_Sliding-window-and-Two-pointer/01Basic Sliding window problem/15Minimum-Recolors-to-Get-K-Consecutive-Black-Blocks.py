'''
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. 
The characters 'W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.


Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
 

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
'''

# Brute force method

class Solution:
    def MinRecolor(self,nums:list[int],k:int) ->int:
        ans =float("inf")

        for i in range(len(nums)):
            white = 0
            for j in range(i,len(nums)):
                if(nums[j]=="W"):
                    white += 1

                length = j-i+1

                if(length==k):
                    ans = min(ans,white)

                    break
        return ans 
nums = "WBWBBBW"
object = Solution()
print(object.MinRecolor(nums,2))

'''
Time Complexity:O(n^2)
Sapce Complexity:O(1)

'''

# Optimal method 
class Solution:
    def MinRecolors(self,nums:list[int],k:int) ->int:
        right,left = 0, 0
        ans = float("inf")
        white = 0
        while(right<len(nums)):
            if(nums[right]=="W"):
                white +=1

            length = right-left+1
            if(length==k):
                ans = min(ans,white)

                if(nums[left]=="W"):
                    white -= 1
                left += 1

            right += 1
        return ans 

nums = "WBWBBBW"
object = Solution()
print(object.MinRecolors(nums,2))

'''
Time Complexity:O(n)
Sapce Complexity:O(1)

'''

                
