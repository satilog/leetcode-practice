from typing import List
from collections import deque

class Solution():
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        def bfs(r: int, c: int) -> int:
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            directions = [ [0, 1], [0, -1], [-1, 0], [1, 0] ]

            while q:
                row, col = q.popleft()            
                for dr, dc in directions:
                    r,c = row+dr, col+dc;

                    if (r in range(rows) and c in range(cols) and grid[r][c]=='1' and (r,c) not in visited):
                        q.append(r,c)
                        visited.add((r,c))
                
            return 1

        for r in rows:
            for c in cols:
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    count += 1
        return 1 