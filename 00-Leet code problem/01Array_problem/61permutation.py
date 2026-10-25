'''
iven an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

class Solution:
    def getper(self,nums,index:int,ans:list[int]):
        if(index==len(nums)):
            ans.append(nums[:])  # nums[:] creates a shallow copy of the current list.
            return

        for i in range(index,len(nums)):
            
            nums[index],nums[i] = nums[i],nums[index]
            self.getper(nums,index+1,ans)

            nums[index],nums[i] = nums[i],nums[index]

    def Permutation(self,nums:list[int]) ->list[list[int]]:
        ans = []
        self.getper(nums,0,ans)

        return ans 
    
nums = [1,2,3]
object = Solution()
print(object.Permutation(nums))


'''
Time Complexity:O(n!*n)
Space Complexity:O(n)

'''

