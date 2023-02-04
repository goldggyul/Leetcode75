class Solution:
    """
    down or right

    같은 것이 있는 순열 -> m, n을 1씩 빼야 하는 걸 주의하자
    """
    def uniquePaths1(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        if m == 0 or n == 0:
            return 1
        numerator = 1
        for num in range(max(m,n)+1, m+n+1):
            numerator *= num
        denominator = 1
        for num in range(2, min(m,n)+1):
            denominator *= num
        return numerator // denominator

    """
    2차원 dp 
    dp[i][j]는 [i][j]번째 까지의 가능한 path 개수
    down, right만 가능하므로 i-1, j-1의 가능한 경우의 수를 더하면 된다
    """
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                dp[i][j] += dp[i-1][j] if i-1>=0 else 0
                dp[i][j] += dp[i][j-1] if j-1>=0 else 0
        return dp[m-1][n-1]

    """
    1차원 dp
    위 2차원 dp식을 자세히 보면
    항상 위/왼쪽 값을 가져오는데, 
    dp[i][j] = dp[i-1][j] + dp[i][j-1]가 되므로
    dp[i][j] = dp[i][j] + dp[i][j-1]가 돼도 상관 없다.
    어차피 [i-1][j]값은 다시 쓰이지 않기 때문이다.
    (플로이드 와샬인가 비슷하게 최적화하던 방법이 있어서 생각남)
    그럼 그냥 일차원으로도 풀 수 있다.
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0]*n
        dp[0] = 1
        for _ in range(m):
            for j in range(n):
                dp[j] += dp[j-1] if j-1>=0 else 0
        return dp[n-1]