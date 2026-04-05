'''
Example 1:
arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Result: True
Explanation: The element 3 is present in the array. So, the answer is True.

Example 2:
arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
Result: False
Explanation: The element 10 is not present in the array. So, the answer is False.
'''
# Brute Force method
class Solution:
    def Search_Rotate_Arr(self,nums:list[int],k:int) -> int:
        for i in range(len(nums)):
            if(nums[i]==k):
                return True
        return False

nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
object = Solution()
print(object.Search_Rotate_Arr(nums,10))  
'''
Time Complixity:O(n)
Space Complixity:O(1)
'''   

# Optimal method
class Solution:
    def SearchRotateArr(self,nums:list[int],k:int) -> bool:
        start = 0
        end = len(nums) -1

        while(start<=end):
            mid = start +(end-start)//2

            if(nums[mid]==k):
                return True
            if(nums[start]==nums[mid]==nums[end]):
                start+=1
                end-=1
                continue

            
            if(nums[start]<=nums[mid]):
                if(nums[start]<=k<=nums[mid]):
                    end = mid-1

                else:
                    start = mid+1

            else:
                if(nums[mid]<=k<=nums[end]):
                    start = mid+1

                else:
                    end = mid-1
        return False
nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
object = Solution()
print(object.SearchRotateArr(nums,6))   

'''
Time Complixity:O(logn)
Space Complixity:O(1)
'''
