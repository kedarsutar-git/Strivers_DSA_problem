'''
Problem Statement: 
Given a string s , consisting only of characters 'a' , 'b' , 'c'.
Find the number of substrings that contain at least 
one occurrence of all these characters 'a' , 'b' , 'c'.



Input : s = "abcba"
Output :  5
Explanation : The substrings containing at least one occurrence of the characters
'a' , 'b' , 'c' are "abc" , "abcb" , "abcba" , "bcba" , "cba".


Input : s = "ccabcc"
Output : 8
Explanation : The substrings containing at least one occurrence of the characters 
'a' , 'b' , 'c' are "ccab" , "ccabc" , "ccabcc" , "cab" , "cabc" , "cabcc" , "abc" , "abcc".
'''

class Solution:
    def countSubstr(self,s:str) ->int:

        count = 0
        for i in range(len(s)):
            res = ""
            for j in range(i,len(s)):
                res += s[j]
                if ("a" in res and "b" in res and "c" in res and len(res)>=3):
                    count += 1

        return count

object = Solution()
s = "ccabcc"
print(object.countSubstr(s))   

'''
Time Complexity:O(n**2)
Space Complexity:O(n)
'''

# optimal method
class Solution:
    def countsunstr(self,s:str) ->int:
        left, right = 0, 0 
        count = 0
        a,b,c = 0 ,0,0 

        while(right<len(s)):
            if(s[right]=="a"):
                a += 1

            elif(s[right]=="b"):
                b += 1

            else:
                c += 1

            
            while(a>0 and b>0 and c>0):
                count += (len(s) -right)
                
                if(s[left]=="a"):
                    a -=1

                elif(s[left]=="b"):
                    b -= 1

                else:
                    c -= 1


                left += 1

            right += 1    
        return count
    
s ="ccabcc"
object = Solution()
print(object.countsunstr(s))     


'''
Time complexity:O(n)
Space complexity:O(1)
'''



                     

        
            


        
