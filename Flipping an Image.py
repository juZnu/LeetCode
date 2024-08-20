class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j] = 0 if image[i][j] else 1
            image[i] = image[i][::-1]
        
        return image
        