"""
https://leetcode.com/problems/two-sum/
follow-up: O(n^2)보다 작은 걸 찾아보자.
소요 시간: 30M

내 풀이
문제에서 '두 개'의 숫자만 고르면 되므로,
한 개를 고정하고 나머지를 binary search로 찾으면 O(nlogn)에 풀 수 있다.
! INF로 -1을 하려면 -1이 입력에 없는 지 잘보자..^^ 이거 때문에 한참 찾음

Solution
1. 처음부터 숫자를 보면서, 다른 숫자가 해쉬맵에 있으면 리턴, 없으면 자기 자신 해쉬맵에 저장
    -> * 이렇게 하면 중복 숫자여도 겹칠 일이 없다. 없으면 그 전에 저장하고 지금 끝났을 거니까.
        따라서 값이 있는 지 없는 지 찾은 다음 해쉬맵 업뎃해야됨.
2. 처음부터 보면서 해쉬맵에 다 저장
    -> 숫자마다 보면서 다른 숫자가 있는 지 확인
       * 중복되면 중복안된 애가 가져갈 것.
3. in을 이용해 있는 지 확인, index를 통해 해당 인덱스 구하기
"""

INF = 10 ** 10


class Solution:
    def findNum(self, nums_with_index: List[int], target: int):
        lo, hi = 0, len(nums_with_index) - 1
        # 인덱스 조심.. lo == hi일 때도 포함!
        while lo <= hi:
            mid = (lo + hi) // 2
            num = nums_with_index[mid][0]
            if num == target:
                return nums_with_index[mid]
            elif num < target:
                lo = mid + 1
            elif num > target:
                hi = mid - 1
        return [INF, INF]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = [(nums[i], i) for i in range(len(nums))]
        nums_with_index.sort()
        for i in range(len(nums)):
            picked = nums_with_index[i]
            found = self.findNum(nums_with_index[i + 1:], target - picked[0])
            if found[0] != INF:
                return [picked[1], found[1]]
        return [INF, INF]
