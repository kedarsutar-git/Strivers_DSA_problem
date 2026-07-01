'''
Problem Statement: Given an array/list of length n where the array/list represents the boards and each element of the given array/list 
represents the length of each board. Some k numbers of painters are available to paint these boards. Consider that each unit of a board 
takes 1 unit of time to paint. You are supposed to return the area of the minimum time to get this job done of painting all the ‘N’ boards 
under the constraint that any painter will only paint the continuous sections of boards.


Example 1:
Input Format: N = 4, boards[] = {5, 5, 5, 5}, k = 2
Result: 10
Explanation: We can divide the boards into 2 equal-sized partitions, so each painter gets 10 units of the 
board and the total time taken is 10.



Example 2:
Input Format: N = 4, boards[] = {10, 20, 30, 40}, k = 2
Result: 60
Explanation: We can divide the first 3 boards for one painter and the last board for the second painter.
'''

class Solution:

    def PaintersPartition(self, bords: list[int], k: int) -> int:
        start = max(bords)
        end = sum(bords)
        ans = -1

        while start <= end:
            mid = start + (end - start) // 2

            if self.is_valid(bords, mid, k):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans

    def is_valid(self, bords, mid, k):
        painter = 1
        totalcard = 0

        for card in bords:
            if totalcard + card <= mid:
                totalcard += card
            else:
                painter += 1

                if painter > k:
                    return False

                totalcard = card

        return True


bords = [10, 20, 30, 40]
obj = Solution()
print(obj.PaintersPartition(bords, 2))              


