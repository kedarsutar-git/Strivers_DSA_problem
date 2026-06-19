# Brute force method 
class Solution:
    def palindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            return False


word = "kedar"

object = Solution()

if object.palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")


'''
Time Complexity:O(n)
Space Complexity:O(n)
'''    

# Optimal method 
class Solution:
    def palindrome(self,s:str) ->bool:
        start , end = 0 , len(s)-1
        while(start<=end):
            if(s[start]!=s[end]):
                return False
            
            start +=1
            end -=1

        return True
s = "madam"
object = Solution()
print(object.palindrome(s))   

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''