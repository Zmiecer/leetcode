class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check(i, j):
            if i > -1 and j > -1 and i < len(grid) and j < len(grid[0]):
                return True
            return False
        
        def containsOne(i, j):
            if check(i, j):
                if grid[i][j] == 1:
                    return 1
            return 0
            
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    p += 4
                    p -= containsOne(i - 1, j) + containsOne(i, j - 1) + containsOne(i + 1, j) + containsOne(i, j + 1)
        return p
                    
