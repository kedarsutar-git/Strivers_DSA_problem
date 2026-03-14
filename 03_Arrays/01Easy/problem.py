# find largest element in the array
class Solution:
    def Largest(self,arr):
        n = len(arr)
        for i in range(n):
            largest = arr[0]
            if(arr[i]>largest):
                largest =arr[i]

        return largest
arr = [5,4,6,7,9,87]
object = Solution()
print(object.Largest(arr))    

    
# cheack the array are sorted or not 
class Solution:
    def cheak(self,arr):
        n = len(arr)
        for i in range(1,n):
            if(arr[i]<arr[i-1]):
                return False

            else:
              return True

arr = [1,2,3,4]
object = Solution()
print(object.cheak(arr))  

# left rotate

class Solution:
    def rotate(self,arr):
        n = len(arr)

        temp = arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]

        arr[n-1]=temp

        return arr  

arr = [1,2,3,4,5]
object = Solution()
print(object.rotate(arr))        

# Rotate the array by left k place
class Solution:
    def kplace(self,arr):
        k = 2
        n = len(arr)
        temp = arr[0:k]
        for i in range(k,n):
            arr[i-k] = arr[i]

        arr[n-k:] =temp

        return arr      
arr = [1,2,3,4,5,6,7,8]
object = Solution()
print(object.kplace(arr))      


# Rotate the array Right k place
class Solution:
    def R_kplace(self,arr):
        k = 2
        n = len(arr)
        temp = arr[n-k:]
        for i in range(n-k-1,-1,-1):
            arr[k+i]=arr[i]

        arr[:k]= temp
        return arr

arr = [5,10,15,25,30]
object = Solution()
print(object.R_kplace(arr))            


for i in range(5,-1,-1):
    print(i)

# liner Search
class Solution:
    def linearSearch(self,arr):
        n = len(arr)
        num = 4
        for i in range(n):
            if(arr[i]==num):
               return arr[i-1]

        return -1    
                
arr = [1,2,3,4,5,6,7,8,9]
object = Solution()
print(object.linearSearch(arr))  


# union of Two sorted array

class Solution:
    def union(self,arr1,arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        s =set()

        for i in range(1,n1+1):
            s.add(i)

        for j in range(1,n1+1):
            s.add(j)   

        l = list(set(s))

        return l
arr1 = [1,2,3,4,5,6]         
arr2 = [4,5,6,6]

object = Solution()
print(object.union(arr1,arr2))


# intersection of Two Sorted array

class Solution:
    def inter(self,arr1,arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        l = []
        for i in range(n1):
            for j in range(n2):
                if(arr1[i]==arr2[j]):
                    if(arr1[i] not in l):
                        l.append(arr1[i])
        return l

arr1 = [1,2,3,4,5]            
arr1 = [3,4,5,6] 

object = Solution()
print(object.inter(arr1,arr2))

# Remove duplicated element from the array

def Remove(arr):
    s = set()
    for num in arr:
        s.add(num)
    l = list(set(s))

    return l
arr = [1,2,2,3,4,5,6,6,7]

print(Remove(arr))

    