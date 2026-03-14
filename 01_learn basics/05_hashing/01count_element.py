arr = []
n1 = int(input("Enter the 1st element:"))
arr.append(n1)

n2 = int(input("Enter the 2nd element:"))
arr.append(n2)

n3 = int(input("Enter the 3rd element:"))
arr.append(n3)

n4 = int(input('Enter the 4th element:'))
arr.append(n4)

n5 = int(input("Enter the  5th element:"))
arr.append(n5)

print(arr)

freq = {}
for element in arr:
    if(element in freq):
        freq[element]+=1

    else:
        freq[element]=1
print(freq)        

