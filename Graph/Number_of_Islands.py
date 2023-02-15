class Solution:
    """
    10M

    '1' 땅 '0' 물
    섬의 개수 대각선 제외하고 인접

    dfs로 한 번 풀고 bfs로 풀었다. bfs가 더 빨랐음
    solution을 보니 섬을 물로 바꾸고 visited 배열을 안 쓰는 방법도 있었다. 코틀린으로 구현함
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER = "0"
        LAND = "1"
        # 범위 계산 생략 위해 padding 추가
        for line in grid:
            line.insert(0, WATER)
            line.append(WATER)
        grid.insert(0, [WATER]*len(grid[0]))
        grid.append([WATER]*len(grid[0]))
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]

        # grid 배열 돌면서 1이면서 not visited인 것에서 dfs
        def bfs(sx, sy):
            visited[sx][sy] = True
            q = deque([(sx, sy)])
            while q:
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if grid[nx][ny] == LAND and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

        island = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[i])-1):
                if grid[i][j] == LAND and not visited[i][j]:
                    bfs(i, j)
                    island += 1
        return island


    def numIslands1(self, grid: List[List[str]]) -> int:
        WATER = "0"
        LAND = "1"
        # 범위 계산 생략 위해 padding 추가
        for line in grid:
            line.insert(0, WATER)
            line.append(WATER)
        grid.insert(0, [WATER]*len(grid[0]))
        grid.append([WATER]*len(grid[0]))
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]

        # grid 배열 돌면서 1이면서 not visited인 것에서 dfs
        def dfs(sx, sy):
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx, ny = sx + dx, sy + dy
                if grid[nx][ny] == LAND and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny)

        island = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[i])-1):
                if grid[i][j] == LAND and not visited[i][j]:
                    visited[i][j] = True
                    dfs(i, j)
                    island += 1
        return island

