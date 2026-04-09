
# Binary search
class Solution:
    def Search(self,nums:list[int],tar:int) ->int:
        start = 0
        end =len(nums)-1
        while(start<=end):
            mid = start+(end - start)//2
            if(nums[mid]==tar):
                return mid
            
            elif(nums[mid]<tar):
                start = mid+1

            else:
                end = mid-1

        return -1


nums = [1,2,3,4,5,6,7,8,9,10]
object = Solution()
print(object.Search(nums,7))


# Lower bound 
'''
arr[index]>=X
arr = [1,2,3,4,5,7]
x = 6

arr[5] >= 6
return 5

'''
class Solution:
    def Lower_bound(self,nums:list[int],X:int) ->int:
        start=  0
        end = len(nums) -1
        while(start<=end):
            mid = start+(end-start)//2
            if(nums[mid]>=X):
                return mid
            
            elif(nums[mid]>X):
                end = mid-1

            else:
                start= mid+1

        return len(nums) 
nums = [1,2,3,4,5,7]

object = Solution()
print(object.Lower_bound(nums,10))

# Upper Bound
'''
nums[index] > X

return index

'''

class Solution:
    def Upper_bound(self,nums:list[int],x:int) ->int:
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = start+(end-start)//2

            if(nums[mid]>x):
                return mid
                end = mid-1

            else:
                start = mid+1

      

nums = [2,5,8,10,16,45]
object =Solution()
print(object.Upper_bound(nums,11))   

# floor and ceil

class Solution:
    def floor_ceil(self,nums:list[int],X:int) -> int:
        for i in range(len(nums)):
            if(nums[i] > X):
                return nums[i-1],nums[i]
            
            elif(nums[i]==X):
                return nums[i],nums[i]
            
nums = [10,20,30,40,50]
object =Solution()
print(object.floor_ceil(nums,25))            

#  first and last occurance
class Solution:
    def first_last(self,nums:list[int],tar:int) ->int:

        def First(nums):
            start = 0
            end = len(nums)-1
            ans = -1
            while(start<=end):
                mid = start+(end-end)//2
                if(nums[mid]==tar):
                    ans = mid
                    end= mid-1
                elif(nums[mid]<tar):
                    start = mid+1   
                else:
                    end = mid-1
            return ans
        def Last(nums):
            start = 0
            end = len(nums)-1
            ans = -1

            while(start<=end):
                mid = start+(end-start)//2

                if(nums[mid]==tar):
                    ans = mid 
                    start = mid+1
                elif(nums[mid]<tar):
                    start = mid+1 
                else:
                    end = mid-1
            
            return ans
        first = First(nums)     
        last = Last(nums)
    
        return [first,last]    

nums = [1,2,3,4,5,5,5,5,6,7,8]
object =Solution()
print(object.first_last(nums,5))  

# Search in Rotate array

class Solution:
    def Search_Rotate(self,nums:list[int],tar:int) ->int:
        start= 0
        end = len(nums)-1

        while(start<=end):
            mid = start +(end-start)//2
            if(nums[mid]==tar):
                return mid

            if(nums[start]<=nums[mid]):
                if(nums[start]<=tar<=nums[mid]):
                    end= mid-1

                else:
                    start = mid+1

            else:
                if(nums[mid]<=tar<=nums[end]):
                    start = mid+1

                else:
                    end = mid-1

        return -1

nums = [1,2,3,4,0]
object =Solution()
print(object.Search_Rotate(nums,10))   

# Find min in the rotated array

class Solution:
    def Find_Min(self,nums:list[int]) -> int:
        






