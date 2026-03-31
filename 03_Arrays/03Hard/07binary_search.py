class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low<=high):
            mid = low +(high-low)//2
            if(nums[mid]==target):
                return mid

            elif(nums[mid]<target):
                low = mid +1

            else:
                high = mid - 1

        return -1
    
nums = [1,2,3,4,5]
object = Solution()
print(object.search(nums,4))    