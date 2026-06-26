# Brute force method 

class Solution:
    def Check_ith_bit(self,n:int,val:int) ->bool:
        res = ""

        while(n>0):
            if(n%2==1):
                res +="1"

            else:
                res +="0"
            n = n//2
        ans = res[::-1]
            
        index = len(ans)-1-val

        if( index<0 ):
            return False
        
        return ans[index] =="1"
            

    
obj = Solution()
print(obj.Check_ith_bit(234,1))    


# Optimal method
class Solution:
    def Check_ith_bit(self, n: int, i: int) -> bool:
        return (n & (1 << i)) != 0


obj = Solution()
print(obj.Check_ith_bit(234, 1))  # True

'''
Time Complexity:O(1)
Space Complexity:O(1)
'''