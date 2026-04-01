# Brute Force method
class Solution:
    def Reverse_Pairs(self,nums:list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(i<j and nums[i]> 2*nums[j]):
                    count +=1

        return count 

nums = [9,8,7,6,5,4,3]
object = Solution()
print(object.Reverse_Pairs(nums))                
'''
Time Complxity :O(n**2)
Space Complixity :O(1)
'''



# Optimal method

class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort(arr, start, end):
            if start>= end:
                return 0
            
            mid = (start + end) // 2
            count = 0
            
            count += merge_sort(arr, start, mid)
            count += merge_sort(arr, mid + 1, end)
            count += count_pairs(arr, start, mid, end)
            
            merge(arr, start, mid, end)
            
            return count
        
        def count_pairs(arr, start, mid, end):
            count = 0
            right = mid + 1
            
            for i in range(start, mid + 1):
                while right <= end and arr[i] > 2 * arr[right]:
                    right += 1
                count += (right - (mid + 1))
            
            return count
        
        def merge(arr, start, mid, end):
            temp = []
            left = start
            right = mid + 1
            
            while left <= mid and right <= end:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            
            while left <= mid:
                temp.append(arr[left])
                left += 1
            
            while right <= end:
                temp.append(arr[right])
                right += 1
            
            for i in range(len(temp)):
                arr[start + i] = temp[i]
        
        return merge_sort(nums, 0, len(nums) - 1) 