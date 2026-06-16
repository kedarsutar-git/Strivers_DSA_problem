'''
Example 1

Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5
Output: 6

Explanation: The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10].
The 5th element of this array is 6.



Example 2

Input: a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7
Output: 256

Explanation: Final sorted array is - [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892], 
7th element of this array is 256.
'''

class Solution:
    def kthElement(self, a:list[int], b:list[int], k:int) ->int:
        i,j,temp = 0,0,[]

        while(i<len(a) and j<len(b)):
            if(a[i]<=b[j]):
                temp.append(a[i])
                i+=1

            else:
                temp.append(b[j])
                j+=1

        while(i<len(a)):
            temp.append(a[i])
            i+=1

        while(j<len(b)):
            temp.append(b[j])
            j+=1

        return temp[k-1]
                          
a = [100, 112, 256, 349, 770]
b = [72, 86, 113, 119, 265, 445, 892]
object = Solution()
print(object.kthElement(a,b,7))

'''
Time Complexity:O(n+m)
Space Complexity:O(1)

'''
