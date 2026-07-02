'''
Problem Statement: ROTI PRATA (SPOJ)
Description:
Given P number of prata (rotis) that need to be cooked and L number of cooks. Each cook has a specific rank (R).
A cook with rank R can cook their first prata in R minutes, the second in 2*R minutes, the third in 3*R minutes,
and so on (the prata takes minutes).

Your task is to determine the minimum time required to cook all P pratas. Cooks can work simultaneously, but a cook
 can only cook one prata at a time.

Example:1

Input:
P (Pratas): 10
L (Cooks): 4
Ranks: [1, 2, 3, 4]
Output: 12
Explanation:
To minimize time, we use Binary Search on the Answer.

The search space for the answer ranges from 0 (best case) to the time taken by the slowest cook to make all pratas (worst case).
For a chosen time we calculate the total number of pratas all cooks can make within that time.
If the sum is we try a smaller time (move left); otherwise, we try a larger time (move right).
In the example above, at 12 minutes:

Cook 1 (Rank 1): Can make 4 pratas (1+2+3+6 = 12 mins is too much, they make 4 within 10 mins: 1+2+3+4).
Cook 2 (Rank 2): Makes 3 pratas (2+4+6 = 12).
Cook 3 (Rank 3): Makes 2 pratas (3+6 = 9).
Cook 4 (Rank 4): Makes 2 pratas (4+8 = 12).
Total: 4 + 3 + 2 + 2 = 11 pratas, which is 
Therefore, 12 is a possible solution.
Constraints:

Each cook acts independently.
A cook must finish one prata before starting the next.
The goal is to minimize the total duration, not the number of cooks used.
'''

class Solution:
    def RotiPrata(self, paratas: int, Cooks: int, Rankes: list[int]):
        start = 0

        Rmax = max(Rankes)
        end = Rmax * (paratas * (paratas + 1) // 2)

        ans = -1

        while start <= end:
            mid = start + (end - start) // 2

            if self.isValid(paratas, Rankes, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans

    def isValid(self, paratas, Rankes, mid):
        Totalpratas = 0

        for rank in Rankes:
            TimeTaken = 0
            j = 1

            while True:
                if TimeTaken + j * rank <= mid:
                    TimeTaken += j * rank
                    Totalpratas += 1
                    j += 1
                else:
                    break

            if Totalpratas >= paratas:
                return True

        return False


obj = Solution()
print(obj.RotiPrata(10, 4, [1, 2, 3, 4]))


'''
Time Complexity:O(nlogn)+O(nlogD)
Space Complexity:O(1)
'''
