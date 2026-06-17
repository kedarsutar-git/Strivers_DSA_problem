class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()

        start = 1
        end = stalls[-1] - stalls[0]

        while(start <= end):
            mid = start + (end - start) // 2

            # Check if we can place k cows with minimum distance = mid
            count = 1
            last_pos = stalls[0]

            for stall in stalls:
                if stall - last_pos >= mid:
                    count += 1
                    last_pos = stall

            if count >= k:
                # Distance is possible, try for a larger one
                start = mid + 1
            else:
                # Distance is not possible
                end = mid - 1

        return end
stalls = [0, 3, 4, 7, 10, 9]
object =Solution()
print(object.aggressiveCows(stalls,3))