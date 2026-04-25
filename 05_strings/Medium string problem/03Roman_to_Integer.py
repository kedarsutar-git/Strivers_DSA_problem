'''
Example 1:
Input:
s = "LVIII"
Output:
58
Explanation:
L = 50, V= 5, III = 3.


Example 2:
Input:
s = "MCMXCIV"
Output:
1994
Explanation:
M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution:
    def RomanToInteger(self,s:str) ->int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = 0
        for i in range(len(s)-1):
            if(roman[s[i]]<roman[s[i+1]]):
                result -= roman[s[i]] 

            else:
                result += roman[s[i]] 

        return result + roman[s[-1]]

s = "LVIII"  
object =Solution()
print(object.RomanToInteger(s))            
'''
Time Complexity:O(n)
Space Compexity:O(1)
'''

            
            