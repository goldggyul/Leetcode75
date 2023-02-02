class Solution:
    """
    두 개의 인접한 집이 같은 날에 털리면 안된다
    오늘밤 훔칠 수 있는 최대

    i번째 집 훔치거나 + 안훔치거나
    대신 전 집을 훔쳤으면 안됨

    dp[i] 정의
    i번째 집을 훔쳤을 때 최대
    dp[i] = max(dp[i-1], dp[i-2]) + nums[i]
    """
    def rob1(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i in range(len(nums)):
            before_2 = dp[i-2] if i-2 >= 0 else 0
            before_3 = dp[i-3] if i-3 >= 0 else 0
            dp[i] = max(before_2, before_3) + nums[i]
        return max(dp)

    """
    # solution 
    i번째에서 오히려 i+1번째를 채운다는 생각을 할 수도 있다!
    여기서 dp[i]의 정의는 i까지 봤을 때의 최대값이다. 그래서 nums[i]가 포함되어 있을 수도 있고 안 되어 있을 수도 있다.
    따라서 dp[i]를 업데이트할 때는 (이전 max) + (이전 칸을 안봤을 때 max + 나!)

    (rob1이 더 빠르긴 하다)
    """
    def rob2(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        # i번째에서 다음 칸을 채운다!
        for i in range(1, len(nums)-1):
            dp[i+1] = max(dp[i], dp[i-1] + nums[i+1])
        return dp[len(nums)-1]

    """
    Step 5. Iterative + 2 variables (bottom-up)
    We can notice that in the previous step we use only memo[i] and memo[i-1], so going just 2 steps back. We can hold them in 2 variables instead. This optimization is met in Fibonacci sequence creation and some other problems [to paste links].

    앗 두번째로 나온 피보나치처럼 두개의 숫자만 유지해도 되는 문젠데 또 생각하지 못했다.
    이번엔 꼭 기억해야지

    + 꼭 바로 아래처럼 2번째 요소부터 시작할 필요 없이 맨 아래처럼 처음부터 시작해도 된다!
    그래도 이게 가장 빠르다?
    """
    def rob3(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        prev1 = max(nums[0], nums[1])
        prev2 = nums[0]
        for i in range(2, len(nums)):
            cur_max_money = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, cur_max_money
        return prev1

    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for num in nums:
            cur_max_money = max(prev1, prev2 + num)
            prev2, prev1 = prev1, cur_max_money
        return prev1

