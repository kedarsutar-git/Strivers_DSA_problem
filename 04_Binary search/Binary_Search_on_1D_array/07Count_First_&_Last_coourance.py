'''
Example 1:
arr = [2, 2 , 3 , 3 , 3 , 3 , 4] ,X=3
Output: 4 

Explanation:
3 is occurring 4 times in 
the given array so it is our answer.




Example 2:
arr = [1, 1, 2, 2, 2, 2, 2, 3],X = 2
Output: 5

Explanation:
2 is occurring 5 times in the given array so it is our answer.

'''
# Brute Force method
class Solution:
    def CountFirst_last_postion(self,nums:list[int],target:int):
        first = 0
        last = 0 
        for i in range(len(nums)):
            if(nums[i]==target):
                if(first==0):
                    first = i
            last = i

        return last-first

nums = [2, 2 , 3 , 3 , 3 , 3 , 3 , 4] 
object = Solution()
print(object.CountFirst_last_postion(nums,3))               

'''
Time Complixity:O(n)
Space complixity:O(1)
'''


# Optimal method

class Solution:
    def Count_First_last_occ(self,nums:list[int],target:int) ->int:

        def first(nums):
            start = 0
            end = len(nums)-1
            ans = -1

            while(start<=end):
                mid = start+(end-start)//2

                if(nums[mid]==target):
                    ans = mid
                    end = mid -1

                elif(nums[mid]>target):
                    end = mid-1

                else:
                    start = mid+1

            return ans


        def last(nums):
            start = 0
            end= len(nums)-1
            ans = -1

            while(start<=end):
                mid = start+(end-start)//2

                if(nums[mid]==target):
                    ans = mid
                    start = mid+1


                elif(nums[mid]>target):
                    end = mid-1

                else:
                    start = mid+1

            return ans    

        First = first(nums)
        Last = last(nums)

        return (Last-First)+1

nums = [2, 2 , 3 , 3 , 3 , 3 , 3 , 4] 
object = Solution()
print(object.Count_First_last_occ(nums,3))               
'''
Time Complexity:O(logn)
Space Complexity:O(1)
'''