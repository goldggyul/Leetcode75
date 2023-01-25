class Solution:
    """
    문제에서 O(n)만에 해결하라 했으므로
    뭔가 이전 값을 활용해야할 것 같았다.
    그래서 적다보니 반복되는 규칙이 있어서 규칙을 활용했다.
    """

    def countBits(self, n: int) -> List[int]:
        answer = [0, 1]
        std = 2
        for i in range(2, n+1):
            if i == std * 2:
                std *= 2
            answer.append(1 + answer[i-std])
        return answer[:n+1]
