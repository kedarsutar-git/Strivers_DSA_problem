class Solution:
    def countsetbits(Self,n:int)->int:
        
        res = ""
        while(n>0):
            if(n%2==1):
                res +="1"

            else:
                res +="0"
            n = n//2

            count = 0
            for i in range(len(res)):
                if(res[i]=="1"):
                    count +=1

        return count
object = Solution()
print(object.countsetbits(13))            

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''

#Optimal method

class Solution:
    def Countsetbits(Self,n:int) ->int:
        count = 0
        while(n!=0):
            n = n &(n-1)
            count +=1

        return count 
object = Solution()
print(object.Countsetbits(13))  

'''
Time Complexity:O(no_of_set_bits)
Space Complexity:O(1)

'''