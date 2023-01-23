class Solution:
    # 19M

    """
    문제를 읽고 N을 보니 10^5라서 N^2엔 안될 것 같았다.
    그러면 이진탐색? NlogN?을 생각했는데 정렬할 방법이 없어서 패스했다.
    그럼 최대값이니까 greedy?를 생각했는데 역시 가장 좋은 걸 선택할 방법이 없었다.
    그럼 dp?를 생각했는데 이거 역시도 떠오르지 않았다.
    그리고 마지막으로 그림을 그려서
    "사이의 값"을 계산하는 거니까
    맨 처음에 가장 처음 / 가장 마지막을 선택하고 좁혀나간다고 생각하니까
    너비가 좁아지면 높이가 높아질 때만 무조건 물이 더 많아질 가능성이 있으니까
    양쪽에서 더 높은 막대쪽으로 가운데로 이동하는 식으로 계산하면 될 것 같았다
    그래서 정답!

    2번째 방법으로 하나씩 이동하는 게 아니라 더 높은 높이를 찾고 이동하는 걸로 하니까
    좀 더 빨라졌지만 메모리를 많이 썼다.

    처음에 너무 어렵다고 생각했는데 쓸 수 있는 알고리즘을 하나씩 생각하니까 의외로 금방 풀렸다!
    """

    def maxArea(self, height: List[int]) -> int:
        def calculateArea(i, j):
            return min(height[i], height[j]) * abs(i - j)

        lo, hi = 0, len(height) - 1
        ans = 0
        while lo < hi:
            ans = max(ans, calculateArea(lo, hi))
            if lo + 1 == hi:
                break
            if height[lo] < height[hi]:
                lo += 1
            elif height[lo] > height[hi]:
                hi -= 1
            else:  # 같을 땐 둘 다 이동
                lo += 1
                hi -= 1
        return ans

    def maxArea2(self, height: List[int]) -> int:
        def calculateArea(i, j):
            return min(height[i], height[j]) * abs(i - j)

        def getNextHighest(current, direction):
            next = current
            while height[next] <= height[current]:
                next += direction
                if not (0 <= next < len(height) - 1):
                    return -1
            return next

        lo, hi = 0, len(height) - 1
        ans = 0
        while 0 <= lo < hi < len(height):
            ans = max(ans, calculateArea(lo, hi))
            if lo + 1 == hi:
                break
            if height[lo] < height[hi]:
                lo = getNextHighest(lo, 1)
            elif height[lo] > height[hi]:
                hi = getNextHighest(hi, -1)
            else:  # 같을 땐 둘 다 이동
                lo = getNextHighest(lo, 1)
                hi = getNextHighest(hi, -1)
        return ans
