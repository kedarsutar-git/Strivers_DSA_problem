'''
1002. Replace Elements by Their Rank
Given an array of N integers, replace each element by its rank in the array. The rank is defined as the position of the element in the sorted unique array (1-based).

Smaller numbers have smaller ranks.
Duplicate elements have the same rank.
The output array should contain the ranks corresponding to each element in the original order.
Example 1:
Input: arr = [20, 15, 26, 2, 98, 6]

Output: [4, 3, 5, 1, 6, 2]

Explanation:

Sorted unique array is [2, 6, 15, 20, 26, 98]
Ranks: 2 → 1, 6 → 2, 15 → 3, 20 → 4, 26 → 5, 98 → 6
Example 2:
Input: arr = [1, 5, 8, 15, 8, 25, 9]

Output: [1, 2, 3, 5, 3, 6, 4]

Explanation:

Sorted unique array: [1, 5, 8, 9, 15, 25]
Ranks: 1 → 1, 5 → 2, 8 → 3, 9 → 4, 15 → 5, 25 → 6
'''
# Brute force method
class Solution:
    def arrayRankTransform(self, nums: list[int]) -> list[int]:
        temp = []
        ans = []
        for i in range(len(nums)):
            temp.append(nums[i])
            temp.sort()

        unique = []
        for i in range(len(temp)):
            if(i==0 or temp[i]!=temp[i-1]):
                unique.append(temp[i])


        for i in range(len(nums)):
            for j in range(len(unique)):
                if(nums[i]==unique[j]):
                    ans.append(j+1)
                    break

        return ans 
        
        

nums = [1, 5, 8, 15, 8, 25, 9]
object = Solution()
print(object.arrayRankTransform(nums))

'''
Time Complexity:O(nlogn)+O(n^2)
Space Complexity:O(n)
'''

# Optimal solution
class Solution:
    def arrayRankTransform(self, nums: list[int]) -> list[int]:
        # Get unique elements and sort them
        temp = sorted(set(nums))

        # Store rank of each element
        rank = {}

        for i, num in enumerate(temp):
            rank[num] = i + 1

        # Generate answer
        ans = []

        for num in nums:
            ans.append(rank[num])

        return ans


nums = [1, 5, 8, 15, 8, 25, 9]

obj = Solution()
print(obj.arrayRankTransform(nums))

'''
Time Complexity: O(n log n)
Space Complexity: O(n)
'''