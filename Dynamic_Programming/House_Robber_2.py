class Solution:
    """
    전 문제와 다른 건 집이 원형으로 이루어져 있다.
    -> 즉 맨 처음 집과 맨 마지막 집을 생각해야 한다.

    그럼 그냥 단순하게 마지막집을 빼고 계산 + 첫 집을 빼고 계산 후에
    최대값을 구하면 된다.

    ! 코너케이스 주의: 원소 하나일 때 첫집 빼고 마지막집 빼면 아무것도 남지 않는다.
    """

    def rob1(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def get_max_money(moneys: List[int]):
            prev1 = 0
            prev2 = 0
            for money in moneys:
                cur_max_money = max(prev1, prev2 + money)
                prev2, prev1 = prev1, cur_max_money
            return prev1

        return max(get_max_money(nums[:len(nums) - 1]), get_max_money(nums[1:]))

    """
    Solution
    
    뭔가 다른 방법이 있나 했지만 원형일땐 시작점이 없으므로
    첫 집과 마지막집을 각각 빼놓고 구하는 방법밖에 없나 보다. 기억해두기~

    * slice 역시 시간과 공간이 든다는 걸 기억해두자. slice할 필요 없이 인덱스만 있어도 된다.
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def get_max_money(start: int, end: int):
            prev1 = 0
            prev2 = 0
            for i in range(start, end):
                cur_max_money = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, cur_max_money
            return prev1

        return max(get_max_money(0, len(nums) - 1), get_max_money(1, len(nums)))
