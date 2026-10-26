'''
Given an array of N intervals in the form of (start[i], end[i]), where start[i] is the starting point of the interval and end[i] is the ending point of the interval, return the minimum number of intervals that need to be removed to make the remaining intervals non-overlapping.

Note:

Intervals which only touch at a point are also considered as non-overlapping. For example, [1, 3] and [3, 4] are non-overlapping.

Example 1:
Input : Intervals = [ [1, 2] , [2, 3] , [3, 4] ,[1, 3] ]

Output : 1

Explanation : You can remove the interval [1, 3] to make the remaining interval non overlapping.

Example 2:
Input : Intervals = [ [1, 3] , [1, 4] , [3, 5] , [3, 4] , [4, 5] ]

Output : 2

Explanation : You can remove the intervals [1, 4] and [3, 5] and the remaining intervals becomes non overlapping.

Now Your Turn!
Pick the correct output for the given input
Input : Intervals = [ [1, 10] , [1, 4] , [3, 8] , [3, 4] , [4, 5] ]


1

2

3

4
Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

Constraints:
1 <= Intervals.length <= 105
0 <= start[i] < end[i] <= 105
Intervals[i].length = 2
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # intervals.sort(key = lambda x :(x[1],x[0]))

        count = 1
        last_num = intervals[0][1]
        for i in range(len(intervals)):
            if(intervals[i][0]>=last_num):
                count += 1

                last_num = intervals[i][1]

        return (len(intervals)) - count 
    
intervals = [[1,2],[1,2],[1,2]]
object = Solution()
print(object.eraseOverlapIntervals(intervals))

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''