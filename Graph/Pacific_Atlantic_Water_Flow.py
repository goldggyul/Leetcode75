class Solution:

    """
    여러 상황이 조합돼있을때 너무 한번에 해결하려고 하지 말고
    나누고 나중에 합쳐보기
    """

    # dfs : 조금 더 빠르다
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacific = [[False] * col for _ in range(row)]
        atlantic = [[False] * col for _ in range(row)]

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def reverseFlow(ocean, x, y):
            ocean[x][y] = True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < row and 0 <= ny < col) or ocean[nx][ny] or heights[nx][ny] < heights[x][y]:
                    continue
                reverseFlow(ocean, nx, ny)

        for j in range(col):
            reverseFlow(ocean=pacific, x=0, y=j)
            reverseFlow(ocean=atlantic, x=row - 1, y=j)
        for i in range(row):
            reverseFlow(ocean=pacific, x=i, y=0)
            reverseFlow(ocean=atlantic, x=i, y=col - 1)

        ans = []
        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans

    # bfs
    def pacificAtlantic1(self, heights: List[List[int]]) -> List[List[int]]:
        # 거꾸로 바다에서부터 같거나 높은 곳으로 퍼진다
        row, col = len(heights), len(heights[0])
        pacific = [[False] * col for _ in range(row)]
        atlantic = [[False] * col for _ in range(row)]

        q = deque()
        for i in range(row):
            for j in range(col):
                # 각 바다에 도달할 수 있는 곳 True로 바꾸고, 갱신됐으면 큐에 넣음
                if i == 0 or j == 0:
                    pacific[i][j] = True
                if i == row - 1 or j == col - 1:
                    atlantic[i][j] = True
                if pacific[i][j] or atlantic[i][j]:
                    q.append((i, j))

        def update(nx, ny, ocean, value):
            if not value:
                return False
            if ocean[nx][ny] != value:
                ocean[nx][ny] = value
                return True
            return False

        differs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            cx, cy = q.popleft()
            for dx, dy in differs:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < row and 0 <= ny < col) or heights[cx][cy] > heights[nx][ny]:
                    continue
                if update(nx, ny, pacific, pacific[cx][cy]) or update(nx, ny, atlantic, atlantic[cx][cy]):
                    q.append((nx, ny))

        ans = []
        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans
