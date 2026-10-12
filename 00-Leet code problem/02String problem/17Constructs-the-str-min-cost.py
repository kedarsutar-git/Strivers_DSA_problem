'''
Given a string target, an array of strings words, and an integer array costs of the same length. You start with an empty string s and can perform the following operation any number of times to construct target with minimal cost:

Choose an index i in the range [0, words.length - 1].
Append words[i] to s.
The cost of the operation is costs[i].
The goal is to construct target using the given words while minimizing the total cost. If it is not possible to construct target, return -1.

Example 1:
Input: target = "qwerty", words = ["qwrty","qwe","r","rty","ty"], costs = [100,1,1,10,5]  

Output: 7  

Explanation:

Append "qwe" (cost = 1) → s = "qwe"

Append "r" (cost = 1) → s = "qwer"

Append "ty" (cost = 5) → s = "qwerty"

Total cost = 1 + 1 + 5 = 7

Example 2:
Input: target = "mmmm", words = ["s","ss","sss"], costs = [1,10,100]  

Output: -1  

Explanation:

None of the words contain "m", so it's impossible to construct "mmmm".

Return -1.
'''

class Solution:
    def minimumCost(self, target: str, words: list, costs: list) -> int:
        s = ""
        ans = 0
        i = 0
        j = 0
        while(i<len(words) and j<len(costs)):
            if(words[i] in target):
                s += words[i]
                ans += costs[j]
            i += 1
            j += 1
        return ans if s == target else -1

object = Solution()
words = ["qwrty","qwe","r","rty","ty"]
costs = [100,1,1,10,5]
target = "qwerty"
print(object.minimumCost(target, words, costs))


         


        