'''
1. Brute Force Approach

Compare every interval with every other interval and merge

'''
def merge_bruteforce(intervals):
    n = len(intervals)
    visited = [False] * n
    result = []

    for i in range(n):
        if visited[i]:
            continue

        start, end = intervals[i]

        for j in range(i + 1, n):
            if not visited[j]:
                s, e = intervals[j]

                # check overlap
                if not (end < s or e < start):
                    start = min(start, s)
                    end = max(end, e)
                    visited[j] = True

        result.append([start, end])

    return result

intervals = [[1,3], [2,6], [8,10], [15,18]]
print("Brute Force:", merge_bruteforce(intervals))




'''
2. Better Approach (Sorting + Merge)

Sort intervals and merge sequentially

'''
def merge_better(intervals):
    intervals.sort()  # sort by start time
    result = []

    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result

intervals = [[1,3], [2,6], [8,10], [15,18]]
print("Better Approach:", merge_better(intervals))




'''
3. Optimal Approach

In interviews, this is considered the optimal solution

'''
class Solution:
    def merge(self, intervals):
        intervals.sort()
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

intervals = [[1,3], [2,6], [8,10], [15,18]]
obj = Solution()
print("Optimal Approach:", obj.merge(intervals))