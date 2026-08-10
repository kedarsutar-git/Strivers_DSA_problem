'''
Bubble Sort Working:

1.Bubble Sort compares adjacent elements in the array.
2.If the left element is greater than the right element, they are swapped.
3.After one complete pass, the largest unsorted element moves to the end of the array.
4.This process repeats for all remaining elements until the array becomes sorted.
'''


class Solution:
    def Sort(self,nums:list[int])->list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)-1):
                if(nums[j]>nums[j+1]):
                    nums[j],nums[j+1],nums[j+1],nums[j]

        return nums
nums = [2,3,4,9,7,6]
object = Solution()
print(object.Sort(nums))

'''
Time Complexity:O(n**2)
Space Complexity:O(1)
'''


