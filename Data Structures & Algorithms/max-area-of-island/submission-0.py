class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs approach
        # recursion
        # when we find a 1, recursively search for all surrounding cells
        # if it is one, add to a count and return the highest value
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set() # making array for visited values from dfs
        res = 0
        maxArea = 0
        area = 0

        def dfs(i,j):
            # base case
            if (i,j) in visited or i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0
            
            visited.add((i,j))
            return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1) 


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = dfs(i,j)
                    if maxArea < area:
                        maxArea = area
        return maxArea
        
        