class Solution:
    """
    앞에 이어서 곱하기 vs. 그냥 나부터 곱하기
    1. 처음에 틀림 -> '곱하기'이므로 마이너스 -> 플러스되는 순간을 생각했어야함
    """
    def maxProduct2(self, nums: List[int]) -> int:
        maxCumulative = 1
        minCumulative = 1
        maxValue = -10
        for num in nums:
            nextMaxCumulative = max(max(maxCumulative * num, minCumulative * num), num)
            nextMinCumulative = min(min(maxCumulative * num, minCumulative * num), num)
            maxCumulative = nextMaxCumulative
            minCumulative = nextMinCumulative
            maxValue = max(maxValue, maxCumulative)
        return maxValue

    """
    * Solution

    0이 나오면 그냥 거기서부터 다시 계산하면 된다
    그리고 그냥 **순차적으로** 곱하면서 최대값인지 업데이트 하면 된다
    만약 음수가 홀수개 있었다면 그걸 곱하기 전인 왼쪽이든 오른쪽에서든 최대값이 답이 될 것이다
    그래서 그냥 왼쪽 오른쪽에서 곱해가면서 보면 된다.

    * or 연산을 통해 0일 때는 1을 곱하도록 할 수 있다
    """
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        prefix = 0
        suffix = 0
        for i in range(0, len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[len(nums)-1-i]
            ans = max(ans, max(prefix, suffix))
        return ans