class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        ## M1: Count each side one by one - O(R*C) - Best
        # Check values adjacent to ones.
        # If a one is at a boundary then that sides auto-contributes to perimeter
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    if (i>0 and grid[i-1][j]==0) or (i==0): # Upper
                        peri +=1
                    if (j>0 and grid[i][j-1]==0) or (j==0): # Left
                        peri +=1
                    if (i<len(grid)-1 and grid[i+1][j]==0) or (i==len(grid)-1):
                        peri +=1 # Lower
                    if (j<len(grid[i])-1 and grid[i][j+1]==0) or (j==len(grid[i])-1):
                        peri +=1 # Right
        return peri

        '''
M2: Shared Edge Subtraction  - O(R*C) - But ~2 times faster

> Every land cell (1) starts by contributing +4 to the perimeter.
> Instead of checking all 4 neighbors, only check top (i - 1) and left (j - 1).
> Whenever two land cells share an edge, that shared border disappears from both cells—so subtract 2 from the perimeter.

        rows, cols = len(grid), len(grid[0])
        peri = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    peri += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        peri -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        peri -= 2
                        
        return peri
        '''