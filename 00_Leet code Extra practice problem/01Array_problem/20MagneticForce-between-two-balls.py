'''
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if 
they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], 
Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force 
between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

 

Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between 
ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.


Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 105
1 <= position[i] <= 109
All integers in position are distinct.
2 <= m <= position.length
'''

class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()

        start = 1
        end = position[len(position)-1] - position[0]
        ans = -1

        while(start<=end):
            mid = start + (end - start)//2

            if(self.isValid(mid,m,position)):
                ans = mid

                start  = mid + 1

            else:
                end = mid - 1

        return ans 

    def isValid(self,mid,m,position):
        pos = 0
        count = 1
        for i in range(1,len(position)):
            if(position[i]-position[pos]>=mid):
                count +=1
                pos = i

                if(count==m):
                    return True 

        return False

object = Solution()

nums =  [5,4,3,2,1,1000000000]
print(object.maxDistance(nums,2))         

'''
Time Complexity:O(nlogn)+O(nlonD)
space Complexity:O(1)

'''