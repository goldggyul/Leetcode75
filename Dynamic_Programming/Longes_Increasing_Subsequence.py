class Solution:
    """
    28M

    lo를 0으로했다가 음수일 때 0보다 작으니까 그 때 문제가 있었다 ..^^
    범위 잘 잡자

    당연히 예전에 풀어봤지만... 기억 안나서 손으로 써보다가 기억이 났다.
    근데 LCS 문제도 한 이십분 봤는데 어떻게 풀더라..

    처음엔 나보다 작은 것 중 가장 큰거 찾아서 걔 다음 넣으려고 했는데
    작은 거 찾을 땐 무한루프를 돌 거 같아 나보다 같거나 큰 걸 찾고
    그 값을 갱신하는 걸로 바꿨다.

    lower bound: 찾고자하는 값 이상이 처음으로 나오는 위치.
    upper bound: 찾고자 하는 값보다 큰 값이 처음으로 나타나는 위치
    따라서 여기선 lower bound를 찾았다.

    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # index: length, element: last number
        dp = [0, nums[0]]
        for i in range(1, n):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                continue
            if dp[-1] == nums[i]:
                continue
            # dp 배열에서 나보다 같거나 큰 것중 가장 작은 것 찾는다
            lo, hi = 1, len(dp) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if dp[mid] >= nums[i]:
                    hi = mid
                else:
                    lo = mid + 1
            if dp[lo] < nums[i]:
                dp.append(nums[i])
            else:
                dp[lo] = min(dp[lo], nums[i])
        return len(dp) - 1
