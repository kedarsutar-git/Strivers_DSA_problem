def rev_arr(arr,start,end):
    if(start>=end):
        return
    
    arr[start],arr[end]=arr[end],arr[start]

    rev_arr(arr,start+1,end-1)
arr =[1,2,3,4,5,6]
rev_arr(arr,0,len(arr)-1)

print(arr)


