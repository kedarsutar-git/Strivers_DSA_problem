class Solution:
    def leftRotateArr(self,nums:list[int] ,k:int) ->int:
          
        temp = nums[0:k]
        for i in range(k,len(nums)):
            nums[i-k]=nums[i]

            nums[len(nums)-k:]=temp
        return nums

nums = [1,2,3,4,5]
object =Solution()
print(object.leftRotateArr(nums,3))    
'''
Time Complexity:O(n)
Space Complexity:O(n)
'''


# optimal approach

class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def leftRotate(self, arr, k):
        n = len(arr)
        k = k % n

        self.reverse(arr, 0, k - 1)
        self.reverse(arr, k, n - 1)
        self.reverse(arr, 0, n - 1)

        return arr


obj = Solution()
arr = [1, 2, 3, 4, 5]
print(obj.leftRotate(arr, 2))
'''
Time Complexity:O(n)
Space Complexity:O(1)
'''

