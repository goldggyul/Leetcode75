class Solution:
    def reverseBits2(self, n: int) -> int:
        result = bin(n)[:1:-1]
        while len(result) < 32:
            result += '0'
        return int(result, 2)

    def reverseBits(self, n: int) -> int:
        answer = 0
        for i in range(32):
            answer <<= 1
            answer |= n & 1
            n >>= 1
        return answer
