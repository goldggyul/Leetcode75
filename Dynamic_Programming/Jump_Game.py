class Solution:
    """
    7M

    nums가 각 지점에서 뛸 수 있는 값이 아닌 뛸 수 있는 '최대값'이므로
    만약 2라면 1칸 갈 수도 있고 2칸 갈 수도 있다.
    만약 dp 배열에 각 칸에 도달할 수 있는 지를 T F로 저장한다 치면
    그럼 M칸 갈수있다면 1~M칸을 모두 봐야하므로
    시간복잡도는 O(10^9)이다. (10^4 * 10^5)
    따라서 다르게 접근한다

    만약 예제1처럼 0번째칸에서 2칸갈 수 있다면 1,2칸에 갈 수 있고
    그 다음 1번째 칸에선 3칸 갈 수 있으므로 1,2,3,4칸에 갈 수 있다.
    그럼 중요한 건 각 칸에서 최댓값만 알면 된다.
    한 칸씩 차례대로 보면서 전 칸에서의 최댓값이 현재 칸의 index보다 작다면
    현재 칸에 도달하지 못하므로 쭉 이동할 수가 없다.
    따라서 그 때 return False를 하면서 마지막까지 도달하면 가능한 것이다.

    근데 위 상황에서 보면 각 칸에서의 최댓값을 저장할 때
    항상 '이전 칸의 최댓값'만 참조한다.
    이 말은 즉 항상 하나의 값만 참조하므로 굳이 배열이 필요 없다는 뜻이다.
    한 칸씩 보면서 현재 상황에서 이동가능 한 최댓값을 업데이트하기만 하면 된다.
    그리고 그 max값이 현재 칸의 index보다 작으면 역시 그 때 return False를 한다.
    """
    def canJump1(self, nums: List[int]) -> bool:
        maxArrive = 0
        for i in range(len(nums)):
            if maxArrive < i:
                return False
            maxArrive = max(i + nums[i], maxArrive)
        return True


    """
    Solution
    거꾸로 뒤에서부터 본다.
    goal에 도착하려면 우선 그 전칸에서 현재 goal에 올 수 있어야 한다.
    그리고 또 그 전칸에 올려면 또 그전칸.... 이렇게 goal을 계속 업데이트한다
    이를 반복해서 최종적으로 goal이 출발점인 0이면 가능하다.
    이게 더 빠르다? max로 더하고 비교해서 업뎃하는 게 없어서 그런가보다
    """
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0