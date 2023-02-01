class Solution:
    # 11M
    # follow-up: 만약 nums에 음수가 있다면?
    # 답이 무한으로 갈 수 있다. -1, 1, -1, 1.... 따라서 길이 제한이든 제한이 있어야 한다
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        # 1부터 target까지
        for i in range(1, target + 1):
            # 가능한 모든 숫자에 대해서
            # 현재 목표값(i) - num을 현재 목표값을 만드는 방법으로 더한다
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]