'''
Given an array nums of size n, which denotes the positions of stalls, 
and an integer k, which denotes the number of aggressive cows, assign 
stalls to k cows such that the minimum distance between any two cows is
the maximum possible. Find the maximum possible minimum distance.


Example 1

Input: n = 6, k = 4, nums = [0, 3, 4, 7, 10, 9]

Output: 3

Explanation:

The maximum possible minimum distance between any two cows will be 3 
when 4 cows are placed at positions [0, 3, 7, 10]. Here the distances
between cows are 3, 4, and 3 respectively.

In no manner can we increase the minimum distance beyond 3.



Example 2

Input : n = 5, k = 2, nums = [4, 2, 1, 3, 6]

Output: 5

Explanation: The maximum possible minimum distance between any two
cows will be 5 when 2 cows are placed at positions [1, 6]. 
'''

class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()

        start = 1
        end = stalls[-1] - stalls[0]

        while(start <= end):
            mid = start + (end - start) // 2

            # Check if we can place k cows with minimum distance = mid
            count = 1
            last_pos = stalls[0]

            for stall in stalls:
                if stall - last_pos >= mid:
                    count += 1
                    last_pos = stall

            if count >= k:
                # Distance is possible, try for a larger one
                start = mid + 1
            else:
                # Distance is not possible
                end = mid - 1

        return end
stalls = [0, 3, 4, 7, 10, 9]
object =Solution()
print(object.aggressiveCows(stalls,3))



class Solution:
    def aggressiveCows(self,nums:list[int],k:int) ->int:
        nums.sort()

        start = 1
        end = nums[len(nums)-1] - nums[0]
        ans =-1
        while(start<=end):
            mid = start + (end - start)//2

            if(self.is_valid(nums,mid,k)):
                ans = mid
                start = mid+1

            else:
                end = mid -1


        return ans   
    

    def is_valid(self,nums,mid,k):
        cowCount = 1
        lastpostion = 0

        for i in range(1,len(nums)):
            if(nums[i]-nums[lastpostion]>=mid):
                cowCount +=1

                lastpostion = i

                if(cowCount==k):
                    return True
                
        return False

object = Solution()
nums =  [0, 3, 4, 7, 10, 9]
print(object.aggressiveCows(nums,3))       
'''
| Operation     | Complexity                     |
| ------------- | ------------------------------ |
| Sorting       | O(nlog n)                      |
| Binary Search | O(log D)                       |
| is_valid()    | O(n)                           |
| Total Time    | O(nlog n + nlog D)             |
| Space         | O(1)                           |
'''



        
    








