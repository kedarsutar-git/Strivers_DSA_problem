'''
Algorithm
1. Add newInterval to the interval list.

2. Sort all intervals by their start time.

3. Create an empty result list for merged intervals.

4. Visit the sorted intervals from left to right and place the first interval directly into the result.

5. If the current interval does not overlap with the last merged interval, append it as a new interval.

6 .Otherwise, merge it by extending the last interval's end, then return the result after all intervals are processed.
'''
# Python program to insert interval using Brute Force sorting
class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        # Add the new interval
        intervals.append(new_interval)
        
        # Sort based on start times
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        # Iterate and merge
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged


object = Solution()
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(object.insert(intervals, new_interval))



'''
Algorithm
1. Start with an empty result list and begin from the first interval.

2. Add every interval whose end is strictly before newInterval starts.

3. Merge every interval whose start is at most the current end of newInterval.

4. After all overlaps are merged, append the updated newInterval to the result.

5. Add all remaining intervals because they start after the merged interval ends.

6. Return the result; empty input naturally returns just the inserted interval.
'''
# Python program to insert interval using single pass optimal approach
class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # Phase 1: Add all intervals completely before the new interval
        while i < n and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1
            
        # Phase 2: Merge all overlapping intervals into one massive interval
        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1
            
        # Add the fully merged new interval
        result.append(new_interval)
        
        # Phase 3: Add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result


object = Solution()
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(object.insert(intervals,new_interval))