'''
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Ex.1:
nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


Ex.2:
nums = [5,7,7,8,8,8,10], target = 6
Output: [-1,-1]


Ex.3:
nums = [], target = 0
Output: [-1,-1]
'''

# Brute Force method
class solution:
    def First_last_occurence(self,nums:list[int],target:int) -> int:
        first = 0
        last =  0
        for i in range(len(nums)):
            if(nums[i]==target):
                if(first== 0):
                    first = i
                last = i        

        return [first,last]
    
nums = [2,4,6,8,8,8,11,13]
object = solution()
print(object.First_last_occurence(nums,8))    

'''
Time Complexity :O(n)
Space Complexity :O(1)

'''
# Optimal method

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def first(nums):
            start = 0
            end = len(nums)-1
            ans =  -1

            while(start<=end):
                mid = start +(end-start)//2
                if(nums[mid]==target):
                    ans = mid
                    end = mid -1   # Searching left

                elif(nums[mid]>target):
                    end =mid-1    # go left

                else:
                    start = mid+1   # go to right 

            return ans

        def last(nums):
            start = 0
            end = len(nums) - 1
            ans = -1
            while(start<=end):
                mid = start +(end-start)//2
                if(nums[mid]==target):
                    ans = mid
                    start = mid+1   # searching right 

                elif(nums[mid]>target):
                    end = mid-1    # go to left

                else:
                    start = mid+1  # go to right 
                    

            return ans
                      
        First  = first(nums)  
        Last = last(nums)

        return [First,Last]

nums  = [1,2,3,3,3,4,5]
object = Solution()
print(object.searchRange(nums,3))           

'''
Time Complexity :O(logn)
Space complexity :O(1)
'''
                                