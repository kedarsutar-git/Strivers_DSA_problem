
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
    def findPages(self, arr, m):
        # Allocation impossible
        if m > len(arr):
            return -1

        start = max(arr)
        end = sum(arr)

        while start <= end:
            mid = (start + end) // 2

            students = 1
            pagesStudent = 0

            for pages in arr:
                if pagesStudent + pages <= mid:
                    pagesStudent += pages
                else:
                    students += 1
                    pagesStudent = pages

            if students > m:
                start = mid + 1
            else:
                end = mid - 1

        return start

arr = [12, 34, 67, 90]    
object =Solution()
print(object.findPages(arr,2))








                    








  
