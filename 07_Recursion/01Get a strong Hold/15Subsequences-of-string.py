class Solution:
    def subseq(self,s:str,index,current,List):
        if(index==len(s)):
            List.append(current)
            return 
        
        self.subseq(s,index+1,current + s[index],List)
    
        self.subseq(s,index+1,current,List) 
    
    

object = Solution()
List = []
object.subseq("abc",0,"",List)

print(List)
                
