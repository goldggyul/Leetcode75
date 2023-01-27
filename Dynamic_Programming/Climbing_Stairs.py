class Solution:
    # 처음에 푼 거
    def climbStairs2(self, n: int) -> int:
        self.dp = [-1] * (n + 1)
        self.dp[0] = 1

        def recursiveClimb(left):
            if left < 0:
                return 0
            if self.dp[left] != -1:
                return self.dp[left]
            ways = recursiveClimb(left - 1)
            ways += recursiveClimb(left - 2)
            self.dp[left] = ways
            return ways

        return recursiveClimb(n)

    # 그 다음 푼 거
    def climbStairs1(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n + 1):
            if i - 1 >= 0:
                dp[i] += dp[i - 1]
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
        return dp[n]

    # 솔루션
    """
    잘 적어보면
    dp[5] = dp[4] + dp[3]
    dp[4] = dp[3] + dp[2]
    피보나치처럼 계속 반복되는 걸 볼 수 있다
    그래서 두가지 변수만 가지고도 가능
    ...
    잘 적어보자!
    """
    # 가장 빠름
    def climbStairs3(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        all_step = 0
        one_step_before = 2
        two_step_before = 1
        for i in range(3, n + 1):
            all_step = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = all_step
        return all_step

    # 메모리 가장 적음
    def climbStairs(self, n: int) -> int:
        current, before = 1, 1
        for _ in range(n):
            current, before = current + before, current
        return before
