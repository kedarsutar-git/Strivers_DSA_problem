
'''
Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, and an integer
m representing the number of students, allocate all the books to the students so that each student gets at least
one book, each book is allocated to only one student, and the allocation is contiguous.

Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized.
If the allocation of books is not possible, return -1.


Example 1

Input: nums = [12, 34, 67, 90], m=2
Output: 113

Explanation: The allocation of books will be 12, 34, 67 | 90.
One student will get the first 3 books and the other
will get the last one.



Example 2

Input: nums = [25, 46, 28, 49, 24], m=4
Output: 71

Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.
'''


class Solution:
    def FindPage(self,nums:list[int],m) ->int:
        if(m>len(nums)):
            return -1 
        
        start = max(nums)
        end = sum(nums)
        ans = -1

        while(start<=end):
            mid = start + (end - start)//2

            if self.isValid(nums,mid,m):
                ans = mid
                
                end = mid - 1

            else:
                start = mid + 1

        return  ans 

    def isValid(self,nums,mid,m):
        student = 1
        totalPages = 0

        for pages in nums:
            if(totalPages+pages<=mid):
                totalPages +=pages

            else:
                student +=1
                totalPages = pages

        if(student>m):
            return False
        return True       

nums = [12, 34, 67, 90]    
object =Solution()
print(object.FindPage(nums,2))









                    








  
