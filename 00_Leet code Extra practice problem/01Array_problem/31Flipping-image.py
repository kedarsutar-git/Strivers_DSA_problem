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