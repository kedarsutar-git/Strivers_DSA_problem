'''
Koko has piles of bananas and h hours to eat them all. She eats at a fixed speed k (bananas/hour).
The goal is to find the minimum speed k so she finishes within h hours.

'''
import math

class Solution:
    def calculateTotalHours(self, piles, speed):
        totalH = 0
        for bananas in piles:
            totalH += math.ceil(bananas / speed)
        return totalH

    def minEatingSpeed(self, piles, h):
        # Find maximum element
        maxPile = max(piles)

        low, high = 1, maxPile
        ans = maxPile

        while low <= high:
            mid = (low + high) // 2
            totalH = self.calculateTotalHours(piles, mid)

            if totalH <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

piles = [3, 6, 7, 11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(piles, h))

'''
Time Complixity:O(n)XO(log(max(pil)))
'''