'''
Given an integer array nums of size n, return the majority element of the array.
The majority element of an array is an element that appears more than n/2 times 
in the array. The array is guaranteed to have a majority element.


Example 1

Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
Output: 7

Explanation:
The number 7 appears 5 times in the 9 sized array



Example 2

Input: nums = [1, 1, 1, 2, 1, 2]
Output: 1

Explanation:
The number 1 appears 4 times in the 6 sized array
'''
# Brute Force method
# Using Two pointer Method
class Solution:
    def Majoritynum(self,nums:list[int]) ->int:
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if(nums[i]==nums[j]):
                    count += 1

            if(count>len(nums)//2):
                return nums[i]
            
        return -1
        

object = Solution()
nums =[2,2,1,1,1,2,2]
print(object.Majoritynum(nums))                   

'''
Time Complexity : O(n**2)
Space Complexity: O(1)
'''


# Better Method
class Solution:
    def Majorityele(self,nums:list[int]) ->int:
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1

            else:
                count_map[num] = 1

        ans = 0
        for key,value in count_map.items():
            if(value>len(nums)//2):
                ans = key

        return ans         
               

object = Solution()
nums = [2,2,1,1,1,2,2]
print(object.Majorityele(nums))


'''
Time Complexity : O(nlog(n))
Space Complexity : O(1)
'''  

# optimal method (Moores Voting Algorithm)
class Solution:
    def majority(self,nums:list[int]) -> int:
        frq = 0
        ans = 0
        for i in range(len(nums)):
            if(frq ==0):
                ans = nums[i]

            if(ans==nums[i]):
                frq+=1

            else:
                frq-=1

        count = 0
        for num in nums:
            if(num==ans):
                count += 1

        if(count>len(nums)//2):
            return ans 

        return -1
            
nums = [1,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4]
object = Solution()
print(object.majority(nums))         
'''
Time Complexity : O(n)
Space Complexity :O(1)

Note : majority element > n/2     n=len(arr)
'''



                    