'''
Example 1:
Input:
 arr = [4, 8, 5, 2, 25]
Output:
 [2, 5, 2, -1, -1]
Explanation:

- For 4, the next smaller element is 2.
- For 8, the next smaller element is 5.
- For 5, the next smaller element is 2.
- For 2, there is no smaller element to its right → -1.
- For 25, no smaller element exists → -1.

Example 2:
Input:
 arr = [10, 9, 8, 7]
Output:
 [9, 8, 7, -1]
Explanation:

Each element’s next right neighbor is smaller.
Each element’s next right neighbor is smaller.
'''

class Solution:
    def nextsmallest(self,nums:list[int]) ->list[int]:
        arr = [-1]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[j]<nums[i]):
                    arr[i] = nums[j]

                    break
        return arr

object = Solution()
nums =[4, 8, 5, 2, 25]
print(object.nextsmallest(nums))

'''
Time Compliexity:O(n*m)
Space Complexity:O(1)

'''

# Optimal method 

class Solution:
    def nextsmallest(self,nums:list[int]) ->list[int]:
        stack =[]
        ans =[-1]*len(nums)

        for i in range(len(nums)-1,-1,-1):

            while(stack and stack[-1]>=nums[i]):
                stack.pop()

            if(stack):
                ans[i] = stack[-1]

            stack.append(nums[i])

        return ans 

object = Solution()
nums =[4, 8, 5, 2, 25]
print(object.nextsmallest(nums))

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''