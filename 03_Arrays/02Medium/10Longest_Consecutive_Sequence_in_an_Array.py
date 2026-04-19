'''
Example 1:
Input:
nums = [100, 4, 200, 1, 3, 2]  
Output:
 4  
Explanation:
The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. This sequence can be formed regardless of the initial order of the elements in the array.

Example 2:
Input:
 nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  
Output:
 9  
Explanation:
 The longest sequence of consecutive elements in the array is [0, 1, 2, 3, 4, 5, 6, 7, 8], which has a length of 9.
'''
# Brute force mthod
class Solution:
    def LongestConsecutive(self,nums:list[int]) ->int:
        nums.sort()
        count , ans = 1 ,1
        prv = nums[0]
       
        for i in range(1,len(nums)-1):
            if(nums[i]==prv+1):
                count +=1

            elif(nums[i]!=prv):
                count =1
            prv = nums[i]

            ans = max(ans,count)
        return ans

object = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(object.LongestConsecutive(nums))               
'''
Time Complexity:O(nlogn)
Space Complexity:O(1)
'''


# optimal method
import math
class Solution:
    def logestConsecutive(self,nums:list[int]) -> int:
        if(len(nums)==0):
            return 0
        
        nums.sort()
        lastSmaller = -math.inf
        count = 0
        longest = 1
        for i in range(len(nums)):
            if(nums[i]-1==lastSmaller):
                count += 1
                lastSmaller = nums[i]

            elif(nums[i]!=lastSmaller):
                count =1
                lastSmaller = nums[i]

            longest = max(longest,count)
        return longest

nums =[100, 4, 200, 1, 3, 2]
object =Solution()
print(object.logestConsecutive(nums))    

'''
Time Complexity:O(n)
space Complexity:O(1)
'''





           