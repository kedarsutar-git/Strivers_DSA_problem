class Solution:
    def Binarysearch(self,nums:list[int],target:int) ->int:
        start = 0
        end = len(nums) - 1
        
        if(nums[start]>nums[end]):
            while(start<=end):
                mid = start + (end - start)//2

                if(nums[mid]==target):
                    return mid
            
                elif(nums[mid]>target):
                    start = mid + 1

                else:
                    end = mid - 1  

        if(nums[start]<nums[end]):
             while(start<=end):
                mid = start + (end - start)//2

                if(nums[mid]==target):
                    return mid
            
                elif(nums[mid]>target):
                    end = mid -1


                else:
                    start = mid +1

        else:
            return -1

nums = [10, 5, 4, 3, 2, 1, 0]
object = Solution()
print(object.Binarysearch(nums,10))                  

'''
Time complexity:O(logn)
Space Complexity:O(1)

'''

        

