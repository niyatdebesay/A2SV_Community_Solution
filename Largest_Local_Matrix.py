class Solution(object):
    def largestLocal(self, grid):
   
        n = len(grid)
        result = [[0 for _ in range(n-2)] for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                max_value = float('-inf')
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        max_value = max(max_value, grid[k][l])
                result[i][j] = max_value

        return result
