from collections import Counter

class Solution:
    """
    Solution
    알파벳 26개 기준으로만 센다
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = [0]*26
        for char in s:
            table[ord(char)-ord('a')] += 1
        for char in t:
            table[ord(char)-ord('a')] -= 1
            if table[ord(char)-ord('a')] < 0:
                return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = Counter(s)
        for char in t:
            if char in counter_s and counter_s[char] > 0:
                counter_s[char] -= 1
            else: 
                return False

        return True


    def isAnagram1(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)

    
