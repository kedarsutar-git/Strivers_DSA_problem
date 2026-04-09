class Solution:
    # Function to check if it's possible to make 'm' bouquets on 'day'
    def is_possible(self, bloom_days, day, m, k):
        count = 0  # count of consecutive bloomed flowers
        bouquets = 0

        for bloom in bloom_days:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0

        return bouquets >= m

    # Main function to find the minimum day to make 'm' bouquets
    def min_days_to_make_bouquets(self, bloom_days, m, k):
        total_flowers = m * k
        if total_flowers > len(bloom_days):
            return -1

        low = min(bloom_days)
        high = max(bloom_days)

        for day in range(low, high + 1):
            if self.is_possible(bloom_days, day, m, k):
                return day

        return -1


bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2

garden = Solution()
result = garden.min_days_to_make_bouquets(bloom_days, m, k)

if result == -1:
    print("We cannot make m bouquets.")
else:
    print(f"We can make bouquets on day {result}")

'''
Time Complixity:O(max-min) X n
space Complixity :O(1)
'''

#optimal method
class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        
        def canMakeBouquets(bloomDay, m, k, day):
            total = 0
            flowers = 0
            for b in bloomDay:
                if b <= day:
                    flowers += 1
                    if flowers == k:
                        total += 1
                        flowers = 0
                else:
                    flowers = 0
                if total >= m:
                    return True
            return False
        
        low, high = 1, max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(bloomDay, m, k, mid):
                high = mid
            else:
                low = mid + 1
        
        return low
        

bloomDay  = [7, 7, 7, 7, 13, 11, 12, 7]
object  = Solution()
print(object.minDays(bloomDay,2,3))

'''
Time Complixty:O(nlogn)
Sapce Complixity:O(1)

'''