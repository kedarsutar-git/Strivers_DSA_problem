class Solution:
    def subseq(self,s:str,index,currentstr,List):
        if(index==len(s)):
            List.append(currentstr)
            return 
        
        self.subseq(s,index+1,currentstr + s[index],List)
    
        self.subseq(s,index+1,currentstr,List) 
    
    

object = Solution()
List = []
object.subseq("abc",0,"",List)

print(List)
                
