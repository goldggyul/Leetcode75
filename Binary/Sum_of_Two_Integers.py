class Solution:
    """
    +나 -를 쓸 수 없으니 비트 연산자로 해결해야 한다.
    비트 연산으로 볼 때, carry가 언제 발생하는가?
    1 + 1일때만 발생한다.
    그럼 둘다 1인건 &연산을 통해 알 수 있다.

    음... 게다가 음수일 때는 문제가 좀 있어서 unsigned로 바꿔줘야 한다.
    solution 안보면 못풀겠다..
    """

    def getSum(self, a: int, b: int) -> int:
        negThresh = 0x80000000
        mask = 0xFFFFFFFF
        # carry가 더 이상 발생하지 않을 때까지
        while b != 0:
            carry = a & b
            a = (a ^ b) & mask
            b = (carry << 1) & mask  # carry를 다음 자리수에서 연산하기 위해선 left shift를 한 번 해줘야 한다.
        if a >= negThresh:
            return ~(a ^ mask)
        else:
            return a
