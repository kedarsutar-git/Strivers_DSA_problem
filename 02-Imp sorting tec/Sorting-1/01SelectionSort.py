'''
Working of Selection Sort:

1.Selection Sort finds the smallest element from the unsorted part of the array.
2.It swaps that element with the first unsorted position.
3.After each pass, one element is placed in its correct sorted position.
4.The process continues until the entire array becomes sorted.
'''

class Solution:
    def SelectionSort(self,nums:list[int]) ->list[int]:
        for i in range(len(nums)):
            Min_index = i
            for j in range(i+1,len(nums)):
                if(nums[j]<nums[Min_index]):
                    Min_index = j

            nums[i],nums[Min_index] = nums[Min_index],nums[i]

        return nums
nums = [12,45,34,89,54,32,87]    
object = Solution()    
print(object.SelectionSort(nums))   
'''
Time Complexity:O(n)
Space complexity:O(1)
'''  
 




        
      