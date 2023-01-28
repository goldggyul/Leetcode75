class Solution:
    """
    dp인 이유? 12^12 시 일단 완탐 불가
    그럼 greedy하게 max만 하냐? -> 정답을 얻을 수 없음
    예) 1, 4, 5 | 13원 => 5, 5, 1, 1, 1 => 5, 4, 4

    만약 1, 2, 5원이 있을 때

    10원을 만드는 개수는
    (9원을 만드는 개수) + 1원
    (8원을 만드는 개수) + 2원
    (5원을 만드는 개수) + 5원
    근데 이게 계속 반복된다. 따라서 dp로 풀 수 있다.

    배열의 정의는 i원을 만드는 동전 갯수이다.
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10_001
        # 최소값 구해야하므로 나올 수 없는 값으로 초기화
        dp = [INF] * (amount + 1)
        # 0원은 0개의 동전으로 만들 수 있다.
        dp[0] = 0
        for coin in coins:
            for cost in range(coin, amount + 1):
                dp[cost] = min(dp[cost], dp[cost - coin] + 1)
        if dp[amount] == INF:
            return -1
        return dp[amount]
