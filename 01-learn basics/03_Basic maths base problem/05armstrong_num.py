class Solution:
    def armstrong(self,num:int,sum:int) ->int:
        dup = num
        order = len(str(num))
        while(num>0):
            digits = num%10
            sum+= digits**order
            num = num//10
        if(sum==dup):
            print("The number is armstrong")
   

        else:
            print("The number is not armstrong")    
            
object = Solution()
print(object.armstrong(153,0))

'''
Time Complexity:O(nlogn)
Space Complexity:O(1)

'''