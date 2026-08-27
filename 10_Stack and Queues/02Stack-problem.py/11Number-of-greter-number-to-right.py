'''
You are given an integer array arr[] of length n and an array of queries indices[] containing positions in arr.



For each query i, determine the number of elements in arr that are strictly greater than arr[indices[i]] and appear to its right (after position indices[i]).



Return an array of answers where the jth value corresponds to the result for indices[j].


Example 1

Input: arr = [3, 4, 2, 7, 5, 8, 10, 6], indices = [0, 5]

Output: [6, 1]

Explanation:

For index 0 → arr[0] = 3, elements greater than 3 to its right are [4, 7, 5, 8, 10, 6] → count = 6.
For index 5 → arr[5] = 8, greater elements to the right are [10] → count = 1.
Example 2

Input: arr = [1, 2, 3, 4, 1], indices = [0, 3]

Output: [3, 0]

Explanation:

For index 0 → arr[0] = 1, greater elements to the right are [2, 3, 4] → count = 3.
For index 3 → arr[3] = 4, no elements greater than 4 exist to the right → count = 0.
'''

class Solution:
    def count_greater_right(self,arr, indices):
        answers = []

        for index in indices:
            count = 0
            for right_index in range(index + 1, len(arr)):
                if arr[right_index] > arr[index]:
                    count += 1
            answers.append(count)

        return answers


arr = [3, 4, 2, 7, 5, 8, 10, 6]
indices = [0, 5]
object = Solution()
print(object.count_greater_right(arr, indices))  
