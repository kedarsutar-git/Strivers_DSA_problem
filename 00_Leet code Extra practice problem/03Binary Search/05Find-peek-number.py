'''
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

 

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

 

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
'''

# Breute force method 
class Solution:
    def peaknumber(self,nums:list[int]) ->int:
        maxnum = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]>maxnum):
                maxnum = nums[i]

        for j in range(len(nums)):
            if(nums[j]==maxnum):
                ans = j

        return ans 

object = Solution()
nums =  [0,2,1,0]
print(object.peaknumber(nums))

'''
Time Complexity:O(n1+n2)
Space Complexity:O(1)
'''


# optimal method 


