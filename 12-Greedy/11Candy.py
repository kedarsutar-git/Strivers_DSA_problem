'''
There are n children standing in a line.

Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

1 <= n == ratings.length <= 5 * 104
0 <= ratings[i] <= 5 * 104
'''

from typing import List

class Solution:
    """
    Finds the minimum candies needed so every child
    satisfies both adjacent rating rules.
    """
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        # Each child must receive at least one candy.
        candies = [1] * n

        for i in range(1, n):
            # If the current child has a higher rating
            # than the left child, they need more candies.
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            # If the current child has a higher rating
            # than the right child, the right-side rule
            # must also be satisfied.
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

ratings = [1,0,2]
object = Solution()
print(object.candy(ratings))


'''
Time Complexity:O(n)
Space Complexity:O(1)

'''