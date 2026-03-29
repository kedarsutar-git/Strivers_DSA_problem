def sub_arr(arr):
    sum = 0
    max = 0
    for i in range(len(arr)):
        sum = sum+arr[i]
        if(sum>max):
            max = sum

        elif(sum<0):
            sum = 0 

    return max 

arr = [-2,1,-3,4,-1,2,1,-5,4] 
print(sub_arr(arr))