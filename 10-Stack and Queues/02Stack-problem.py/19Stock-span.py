'''
Given an array arr of size n, where each element arr[i] represents the stock price on day i. Calculate the span of stock prices for each day.



The span Si for a specific day i is defined as the maximum number of consecutive previous days (including the current day) for which the stock price was less than or equal to the price on day i.


Example 1

Input: n = 7, arr = [120, 100, 60, 80, 90, 110, 115]

Output: [1, 1, 1, 2, 3, 5, 6]

Explanation:

Traversing the given input span:

120 is greater than or equal to 120 and there are no more elements behind it so the span is 1,

100 is greater than or equal to 100 and smaller than 120 so the span is 1,

60 is greater than or equal to 60 and smaller than 100 so the span is 1,

80 is greater than or equal to 60, 80 and smaller than 100 so the span is 2,

90 is greater than or equal to 60, 80, 90 and smaller than 100 so the span is 3,

110 is greater than or equal to 60, 80, 90, 100, 110 and smaller than 120 so the span is 5,

115 is greater than or equal to all previous elements and smaller than 120 so the span is 6.

Hence the output will be 1 1 1 2 3 5 6.

Example 2

Input: n = 6, arr = [15, 13, 12, 14, 16, 20]

Output: [1, 1, 1, 3, 5, 6]

Explanation:

Traversing the given input span:

15 is greater than or equal to 15 and there are no more elements behind it, so the span is 1.

13 is smaller than 15, so the span is 1.

12 is smaller than 13, so the span is 1.

14 is greater than or equal to 12 and 13, but smaller than 15, so the span is 3 (days with values 12, 13, and 14).

16 is greater than or equal to 14, 12, 13, and 15, so the span is 5.

20 is greater than or equal to all previous elements, so the span is 6.

Hence the output will be 1 1 1 3 5 6.
'''


class Solution:
    def stockSpan(self, arr):
        ans = [0]*len(arr)
        for i in range(len(arr)):
            span = 0
            for j in range(i,-1,-1):
                if(arr[j]<=arr[i]):
                    span += 1

                else:
                    break

            ans[i] = span
        
        return ans 

object = Solution()
arr =  [15, 13, 12, 14, 16, 20]
print(object.stockSpan(arr))

'''
Time Complexity:O(n^2)
Space Complexity:O(1)
'''

# Optimal method 
class Solution:
    def calculateSpan(self, prices):
        n = len(prices)
        span = [0] * n
        stack = []  # stores indices of days

        # First day span is always 1
        span[0] = 1
        stack.append(0)

        # Process rest of the days
        for i in range(1, n):
            # Pop elements from stack while price[i] >= price[stack[-1]]
            while stack and prices[i] >= prices[stack[-1]]:
                stack.pop()

            # If stack is empty, price[i] is greater than all previous prices
            span[i] = i + 1 if not stack else (i - stack[-1])

            # Push current day index onto stack
            stack.append(i)

        return span


# Example usage
prices = [100, 80, 60, 70, 60, 75, 85]
sol = Solution()
print(sol.calculateSpan(prices))
'''
Time complexity:O(n)
Space  complexity:O(n)
'''