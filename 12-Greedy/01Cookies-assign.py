'''
Consider a scenario where a teacher wants to distribute cookies to students, with each student receiving at most one cookie.

Given two arrays, student and cookie, the ith value in the Student array describes the minimum size of cookie that the ith student can be assigned. The jth value in the Cookie array represents the size of the jth cookie. If Cookie[j] >= Student[i], the jth cookie can be assigned to the ith student.

Maximize the number of students assigned with cookies and output the maximum number.

Example 1:
Input : student = [1, 2, 3] , cookie = [1, 1]

Output :1

Explanation : You have 3 students and 2 cookies.

The minimum size of cookies required for students are 1 , 2 ,3.

You have 2 cookies both of size 1, So you can assign the cookie only to student having minimum cookie size 1.

So your answer is 1.

Example 2:
Input : student = [1, 2] , cookie = [1, 2, 3]

Output : 2

Explanation : You have 2 students and 3 cookies.

The minimum size of cookies required for students are 1 , 2.

You have 3 cookies and their sizes are big enough to assign cookies to all students.

So your answer is 2.
'''
class Solution:
    def findContentChildren(self, student: list[int], cookie: list[int]) -> int:

        Students = sorted(student)
        Cookies = sorted(cookie)

        left = 0
        right = 0

        while left < len(Students) and right < len(Cookies):

            if Cookies[right] >= Students[left]:
                right += 1
                left += 1
            else:
                right += 1

        return left

student = [1, 2, 3]
cookie = [1, 1]
object = Solution()
print(object.findContentChildren(student,cookie))

'''
Time Complexity:O(nlogm + mlogn + n)
Space Complexity:O(1)

'''