'''
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
'''


'''
Enhanced Breakdown:

1. Initialize and Calculate the Target
   - Compute `target = sum(nums) - x`.
   - Instead of directly removing elements from the ends, we look for the **longest subarray** whose sum equals `target`.
   - Initialize:
     - `max_len = 0` → Stores the length of the longest valid subarray.
     - `cur_sum = 0` → Stores the current window sum.
     - `left = 0` → Left pointer of the sliding window.

2. Check for Edge Case
   - If `target == 0`, it means the entire array sums to `x`.
   - Therefore, all elements must be removed.
   - Return `n` (the length of the array).

3. Traverse the Array Using Two Pointers
   - Move the `right` pointer from left to right through the array.
   - At each step:
     - Add `nums[right]` to `cur_sum`.

4. Adjust the Sliding Window
   - While `cur_sum > target`:
     - Remove `nums[left]` from `cur_sum`.
     - Increment `left` by 1.
   - This keeps the window sum less than or equal to `target`.

5. Update the Maximum Length
   - If `cur_sum == target`:
     - A valid subarray has been found.
     - Update:
       - `max_len = max(max_len, right - left + 1)`
   - Since we need the **minimum operations**, we maximize the length of the subarray we keep.

6. Conclude and Return
   - If `max_len > 0`:
     - Return `n - max_len`.
     - This represents the minimum number of elements removed from both ends.
   - Otherwise:
     - Return `-1`.
     - No valid subarray with sum `target` exists, so reducing `x` to zero is impossible.
'''

class Solution:
    def MinOperations(self,nums:list[int],x:int):
        maxlen = -1
        right,left = 0 ,0 
        target = sum(nums)-x
        currentsum = 0
        if(target==0):
            return len(nums)

        if(target<0):
            return -1

        while(right<len(nums)):
            currentsum+=nums[right]

            while(currentsum>target):
                currentsum-=nums[left]
                left+=1
            if(currentsum==target):
                maxlen = max(maxlen,right-left+1)
            right+=1


        if(maxlen!=-1):
            return len(nums)-maxlen
        return -1

object = Solution()
nums = [1,1,4,2,3]
print(object.MinOperations(nums,5))


