# https://leetcode.com/problems/flood-fill/

# Flood Fill

'''
Input:

image =
[
[1,1,1],
[1,1,0],
[1,0,1]
]
sr = 1, sc = 1, newColor = 2

Output:
[
[2,2,2],
[2,2,0],
[2,0,1]
]
Explanation: From the center of the image with position (sr, sc) = (1, 1)
(i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel
(i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        
        # helper function
        def dfs(r, c):
            if image[r][c] == color:
                #if match found, change to newColor
                image[r][c] = newColor
                #since match found, check in all four directions
                # for up
                if r >= 1:
                    dfs(r-1, c)
                # for down
                if r+1 < rows:
                    dfs(r+1, c)
                # for left
                if c >= 1:
                    dfs(r, c-1)
                # for right
                if c+1 < cols:
                    dfs(r, c+1)
                
        dfs(sr, sc)
        return image
