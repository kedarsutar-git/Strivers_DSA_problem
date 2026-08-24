class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in range(len(image)):
            i = 0
            j = len(image)-1

            while(i<=j):
                image[row][i],image[row][j] = image[row][j],image[row][i]

                i+=1
                j-=1

        for i in range(len(image)):
            for j in range(len(image[0])):
                if(image[i][j]==0):
                    image[i][j] = 1

                elif(image[i][j]==1):
                    image[i][j] = 0

        return image


image = [[1,1,0],[1,0,1],[0,0,0]]
object = Solution()
print(object.flipAndInvertImage(image))

'''
Time Complexity:O(n^2)
Space complexity:O(1)
'''


def matrix_multiplication(a, b): 
    result = [] 
    for i in range(len(a)): 
        row = [] 
        for j in range(len(b[0])): 
            total = 0 
            for k in range(len(b)):  # multiply corresponding values and add them 
                total += a[i][k] * b[k][j] 
            row.append(total) 
        result.append(row) 
    return result 
 

def scalar_multiplication(matrix, scalar): 
    result = [] 
    for row in matrix: 
        new_row = [] 
        for value in row: 
            new_row.append(value * scalar) 
        result.append(new_row) 
    return result 
 
A = [[1, 2], [3, 4]] 
B = [[5, 6], [7, 8]] 
print("A + B:") 

