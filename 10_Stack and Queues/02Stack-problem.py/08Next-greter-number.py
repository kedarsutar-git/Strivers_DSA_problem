'''
Problem:  
Given an array nums of integers, for each element in the array, find the Next Greater Element (NGE) to its right.

The Next Greater Element of an element x is the first element to the right of x in the array that is strictly greater than x.

If no such element exists, output -1 for that position.

Input:

An integer array nums of length n (1 ≤ n ≤ 10^5).

Each element satisfies: -10^9 ≤ nums[i] ≤ 10^9.

Output:

An integer array result of length n, where result[i] is the next greater element of nums[i].

If no greater element exists, result[i] = -1.

Example 1
Code
Input: nums = [4, 5, 2, 25]
Output: [5, 25, 25, -1]
Explanation:
- For 4 → next greater is 5
- For 5 → next greater is 25
- For 2 → next greater is 25
- For 25 → no greater element, so -1
Example 2
Code
Input: nums = [13, 7, 6, 12]
Output: [-1, 12, 12, -1]
Constraints
1 ≤ n ≤ 10^5


'''
class Solution:
    def nextLargerElement(self, arr):
        temp = [-1]*len(arr)
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if(arr[j]>arr[i]):
                    temp[i] = arr[j]
                    break

        return temp

nums = [13, 7, 6, 12]
object = Solution()
print(object.nextLargerElement(nums))
'''
Time Complexity:O(n**2)
Space Complexity:O(n)

'''


# optimal method
class Solution:
    def nextLargerElement(self, arr):
        stack = []
        result = [-1]*len(arr)
        for i in range(len(nums)-1,-1,-1):
            while(len(stack)!=0 and stack[-1]<=arr[i]):
                stack.pop()

            if(len(stack)!=0):
                result[i] = stack[-1]
            stack.append(arr[i])
            
        return result   

object = Solution()
nums = [13, 7, 6, 12]
print(object.nextLargerElement(nums))
'''
Time Complexity:O(n)
Space Complexity:O(n)
'''