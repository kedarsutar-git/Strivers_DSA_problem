
def missing(arr):
        n = len(arr)
        lotalsum = sum(arr)
        N = (n+1)
        expsum = N*(N+1)//2

        return expsum-lotalsum
    
arr = [1,6,5,3,4]

print(missing(arr))    

