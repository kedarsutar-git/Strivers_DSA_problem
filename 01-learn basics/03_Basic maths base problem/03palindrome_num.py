class Solution:
     def palindrome(self,num:int) -> int:
          dup = num
          reversed = 0
          while(num>0):
               m = num%10
               num = num//10
               reversed = (reversed*10)+m
          if(reversed ==dup):
               print("The number is palindrome")

          else:
               print("The number is  not plindrome")
num  = 112
object = Solution()
print(object.palindrome(num))


'''
Time Complexity:O(logn)
Space Complexity:O(1)
'''


