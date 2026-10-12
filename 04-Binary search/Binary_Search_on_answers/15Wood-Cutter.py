'''
Problem: Wood Cutter
Description:
Lumberjack needs to cut down trees for wood. He has a sawmill that can cut trees at a specific height H from the ground. 
If a tree's height is greater than H, the part above H is collected as wood. If a tree's height is less than or equal to 
H, no wood is collected from that tree.

Given an array of integers trees, where trees[i] is the height of the i-th tree, and an integer m representing the minimum 
total units of wood required, determine the maximum integer height H at which the lumberjack can set his saw to collect at 
least m units of wood.


Example:1
Input: trees = [20, 15, 10, 17], m = 7
Output: 15

Explanation:
If the saw is set at height 15:

Tree 1 (20) contributes: 20 - 15 = 5
Tree 2 (15) contributes: 15 - 15 = 0
Tree 3 (10) contributes: 0 (tree is shorter than saw)
Tree 4 (17) contributes: 17 - 15 = 2
Total wood = 5 + 0 + 0 + 2 = 7. Since 7 ≥ 7, 15 is a valid height. Setting the saw higher would result in less wood.
Constraints:

1 <= trees.length <= 1,000,000
1 <= trees[i] <= 1,000,000,000
1 <= m <= 2,000,000,000
'''

class Solution:
    def WoodCutter(self,trees:list[int],m:int) ->int:
        start  = 0
        end = max(trees)
        ans = -1
        while(start<=end):
            mid = start +(end - start)//2

            if self.is_valid(trees,mid,m):
                ans = mid

                start = mid + 1

            else:
                end = mid - 1

        return ans 

    def is_valid(self,trees,mid,m) ->bool:
        totalWood = 0
        for i in range(len(trees)): 
            if(trees[i]>mid):
                totalWood += trees[i] - mid
                
        if(totalWood>=m):
                return True 
                

        return False 

object = Solution()
trees = [20, 15, 10, 17]
print(object.WoodCutter(trees,7)) 

'''
Time Complexity:O(nlogn)+O(nlogD)
Space Complexity:O(1)
'''

