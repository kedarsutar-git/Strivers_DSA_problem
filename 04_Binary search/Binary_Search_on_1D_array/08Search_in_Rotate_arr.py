'''
nums = [1,2,3,4,5,6,7,8] # normal Sorted array

nums = [7,8,1,2,3,4,5,6] # Rotated array

'''
# Brute Force method

class Solution:
    def Search_Rotate_arr(self,nums:list[int],tar:int) -> int:
        for i in range(len(nums)):
            if(nums[i]==tar):
                return i
            
        return -1

nums = [7,8,1,2,3,4,5,6] 
object = Solution()
print(object.Search_Rotate_arr(nums,6)) 

'''
Time Complixity :O(n)
Space Complixity:O(1)
'''

# Optimal method

class Solution:
    def Search_Rotate_Arr(self,nums:list[int],target:int) -> int:
        start = 0
        end = len(nums) -1
        while(start<=end):
            mid = start+(end-start)//2
            if(nums[mid]==target):
                return mid

            if(nums[start]<=nums[mid]):
                if(nums[start]<=target<=nums[mid]):
                    end = mid-1

                else:
                    start = mid+1

            else:
                if(nums[mid]<=target<=nums[end]):
                    start = mid+1

                else:
                    end = mid-1
        

nums = [7,8,1,2,3,4,5,6]
object = Solution()
print(object.Search_Rotate_Arr(nums,1))                         

'''
Time Complixity :O(logn)
Space complixity:O(1)
'''
