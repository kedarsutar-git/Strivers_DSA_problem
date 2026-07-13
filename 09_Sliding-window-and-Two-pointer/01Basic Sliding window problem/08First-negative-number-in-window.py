'''
EX:1

Input: arr[] = [-8, 2, 3, -6, 10] , k = 2
Output: [-8, 0, -6, -6]

Explanation:
Window [-8, 2] First negative integer is -8.
Window [2, 3] No negative integers, output is 0.
Window [3, -6] First negative integer is -6.
Window [-6, 10] First negative integer is -6.



EX:2

Input: arr[] = [12, -1, -7, 8, -15, 30, 16, 28] , k = 3
Output: [-1, -1, -7, -15, -15, 0] 

Explanation:
Window [12, -1, -7] First negative integer is -1.
Window [-1, -7, 8] First negative integer is -1.
Window [-7, 8, -15] First negative integer is -7.
Window [8, -15, 30] First negative integer is -15.
Window [-15, 30, 16] First negative integer is -15.
Window [30, 16, 28] No negative integers, output is 0.


EX:3
Input: arr[] = [12, 1, 3, 5] , k = 3
Output: [0, 0] 
Explanation:
Window [12, 1, 3] No negative integers, output is 0.
Window [1, 3, 5] No negative integers, output is 0.
'''

class Solution:
    def FirstNegative(self, arr: list[int], k: int):
        left = 0
        right = 0

        negative = []
        ans = []

        while right < len(arr):

            # Add negative number to the current window
            if arr[right] < 0:
                negative.append(arr[right])

            # Window size is less than k
            if right - left + 1 < k:
                right += 1

            # Window size becomes k
            elif right - left + 1 == k:

                if len(negative) > 0:
                    ans.append(negative[0])
                else:
                    ans.append(0)

                # Remove the outgoing negative element
                if len(negative) > 0 and arr[left] == negative[0]:
                    negative.pop(0)

                left += 1
                right += 1

        return ans


obj = Solution()

arr = [-8, 2, 3, -6, 10]
print(obj.FirstNegative(arr, 2))

'''
Time Complexity:O(n)
Space Complexity:O(n)

'''
                
                    


