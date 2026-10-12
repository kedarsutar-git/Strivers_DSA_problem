'''
Example 1

Input:
 s = "5347"
Output:
 "5347"
Explanation:
 The odd numbers formed by the given string 
 are → 5, 3, 53, 347, 5347. The largest odd number
 without leading zeroes is 5347.

 
Example 2

Input:
 s = "0214638"
Output:
 "21463"
Explanation:
 The odd numbers formed by the string 
 are → 1, 3, 21, 63, 463, 1463, 21463. We can't use numbers 
 starting with 0, so the largest valid odd number is 21463.
'''


class Solution:
    def LargestOddNo(self,s:str) -> str:
        index = -1
        for i in range(len(s)-1,-1,-1):
            if(int(s[i])%2==1):
                index = i
                break
        i = 0
        while(i<=index  and s[i]=="0"):
            i+=1

        return s[i:index+1]    

s = "4206"
object = Solution()
print(object.LargestOddNo(s))               

'''
Time Complixity:O(n)
space Complixity:O(1)
'''

#using Max 
class Solution:
    def LargestOdd(self,s:str) -> str:
        index = 0
        Max = 0
        for i in range(len(s)-1,-1,-1):
            if(int(s[i])%2==1):
                index = i
                Max = max(index,Max)

        if(Max==0):
            return ""        

        i = 0
        while(i<=Max and s[i]=="0"):
            i+=1

        return s[i:Max+1]
    
s = "4206"
object =Solution()
print(object.LargestOdd(s))




