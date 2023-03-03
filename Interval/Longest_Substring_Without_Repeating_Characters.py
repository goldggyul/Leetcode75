class Solution:
    # 내가 길이를 기억하고 있었다면 solution은 투포인터로 왼쪽을 기억하는 느낌으로
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndex = {}
        maxLength, currentLength = 0, 0
        lo = 0
        for hi in range(len(s)):
            if s[hi] in lastIndex:
                lo = max(lastIndex[s[hi]] + 1, lo)
            lastIndex[s[hi]] = hi
            maxLength = max(maxLength, hi - lo + 1)
        return maxLength

    def lengthOfLongestSubstring1(self, s: str) -> int:
        lastIndex = {}
        maxLength, currentLength = 0, 0
        for i, char in enumerate(s):
            currentLength += 1
            if char in lastIndex:
                if lastIndex[char] > i - currentLength:
                    currentLength = i - lastIndex[char]
            lastIndex[char] = i
            maxLength = max(currentLength,maxLength)
        return maxLength
