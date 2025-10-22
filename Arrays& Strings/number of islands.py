grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


# Itirative DFS
def island(grid):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols= len(grid[0])
    islands =0
   
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=='1' or grid[r][c]==1:
                islands += 1
                stack = [(r,c)]
                while stack:
                    i,j = stack.pop()
                    if grid[i][j] == 0 or grid[i][j]=='0':
                        continue
                    grid[i][j]='0' # mark visited
                    if i-1 >=0 and grid[i-1][j]=='1':
                        stack.append((i-1,j))
                    if i+1 < rows and grid[i+1][j]=='1':
                        stack.append((i+1,j))
                    if j-1 >= 0 and grid[i][j-1]=='1':
                        stack.append((i,j-1))
                    if j+1 < cols and grid[i][j+1]=='1':
                        stack.append((i,j+1))

    return islands

print(island(grid))

def numIslands(grid):
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0' or grid[i][j] == 0:
                return
            grid[i][j] = '0'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' or grid[i][j] == 1:
                    islands += 1
                    dfs(i, j)

        return islands

#numIslands(grid)