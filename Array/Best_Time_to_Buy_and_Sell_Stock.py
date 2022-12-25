"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
9M

사고 팔 때 최대 이익 내기
최소 이익은 0

단순하게 최대/최소를 구하면 안되고, 앞에 있는 날짜가 더 작아야 한다.

1. 최대/최소니까 greedy를 생각해본다.
2. dp, 그래프 탐색 생각하기
처음부터 보면서 각 날짜별로 dp[i] = i번째 날 전까지 최소 금액
을 구한다.
그 후 max(price[i] - dp[i])인 게 정답
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        # i번째 날까지의 최소 금액 구하기
        dp[0] = prices[0]
        for i in range(1, len(prices)):
            dp[i] = min(prices[i], dp[i - 1])
        # 최대 이익 구하기
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - dp[i])
        return max_profit

    """
    Solution:
    내 풀이 같은 경우는 i번째 날까지 최소 금액을 배열로 따로 구했는데,
    굳이 배열을 따로 구할 필요 없이 계속 최소 금액만 구해도 괜찮다.
    """
    def maxProfit_Solution(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit