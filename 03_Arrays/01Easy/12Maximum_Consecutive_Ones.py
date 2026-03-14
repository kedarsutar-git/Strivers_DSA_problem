def Maxcount(arr):
    count = 0
    Max = 0
    for num in arr:
        if(num==1):
            count = count+1
            Max = max(Max,count)

        else:
            count = 0

    return Max

arr = [1,0,0,0,1,1,1,0,0,0,1,1,1,1]
print(Maxcount(arr))            