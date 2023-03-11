class Solution:
    """
    n = 1000

    1. i를 중심으로 하는 팰린드롬
    2. i, i+1 사이를 중심으로 하는 팰린드롬

    - Time complexity: O(n^2)
        -> 정확하겐 n * (2n-1)
        2n - 1은 중심이 될 수 있는 후보 개수
        n 과 그 사이의 n-1
    - Space complexity: O(1)
    """

    def countSubstrings(self, s: str) -> int:
        numberOfPalindrome = 0

        def countPalindromeStartFrom(left: int, right: int):
            numberOfPalindrome = 0
            while 0 <= left <= right < len(s):
                if s[left] != s[right]:
                    return numberOfPalindrome
                numberOfPalindrome += 1
                left -= 1
                right += 1
            return numberOfPalindrome

        for i in range(len(s)):
            numberOfPalindrome += countPalindromeStartFrom(left=i, right=i)
            numberOfPalindrome += countPalindromeStartFrom(left=i, right=i + 1)
        return numberOfPalindrome