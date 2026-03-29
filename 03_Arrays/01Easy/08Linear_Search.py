def Linear_Search(arr):
    n = len(arr)
    num = 9
    for i in range(n):
            if(arr[i]==num):
                return i
    else:
        return -1
arr = [1,2,3,4,5,6,7,8,9]
print(Linear_Search(arr))                


# leet code style 
class Solution:
     def linerSearch(self,nums:list[int]) -> int:
          n = 439
          for i in range(len(nums)):
               if(nums[i]==n):
                    return i
          else:
               return -1
nums = [1,2,3,4,5,43]
object = Solution()
print(object.linerSearch(nums))                