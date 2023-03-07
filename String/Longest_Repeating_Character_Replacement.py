from collections import defaultdict

class Solution:
    """
    Solution
    **윈도우 크기를 줄일 필요가 없다!**
    만약 길이 l이 가능하다면, 굳이 l-1 길이로 줄일 필요가 없다.
    길이 l이 가능하면 l의 크기를 유지하면서 가능할 때 l+1로 늘리면 되는 것이다.
    따라서 탐색이 끝났을 때 윈도우의 크기가 가능한 길이이다.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        start = 0
        max_frequency = 0
        for end in range(len(s)):
            frequency[s[end]] += 1
            max_frequency = max(max_frequency, frequency[s[end]])
            if (end - start + 1) - max_frequency > k:
                frequency[s[start]] -= 1
                start += 1
        return len(s) - start

    
    def isLengthValid(self, s:str, k:int, length:int) -> bool:
        frequency = defaultdict(int)
        max_frequency = 0
        start = 0
        for end in range(len(s)):
            frequency[s[end]] += 1
            # window보다 커지면 조절
            if end - start + 1 > length:
                frequency[s[start]] -= 1
                start += 1
            max_frequency = max(max_frequency, frequency[s[end]])
            # 현재 윈도우가 length길이가 아니더라도 조건만 만족한다면 상관 없음
            if length - max_frequency <= k:
                return True
        return False
    
    """
    Solution

    **이분 탐색**을 이용한다. 이 때 이분 탐색으로 길이를 찾는다.
    만약 길이 l이 가능하다면 길이 l-1, l-2, ... 1까지 모두 가능하다.
    따라서 이 특성을 이용한다!

    이 때 그 길이가 가능한 지 판단하는 isLengthValid 함수를 보면,
    내가 매번 한 알파벳만 확인했던 것과 달리 
    모든 문자의 frequency를 기록해서 max frequency와 나머지로 구분해서 
    k를 넘었는 지 판단한다.

    그리고 max_frequency를 그 윈도우에서의 최대가 아닌 이때까지 본 최대 빈도수로 유지하는데,
    어차피 max_frequency와 k 관계가 만족되는 순간 정답으로 구할 수 있으니까
    상관이 없다.
    """
    def characterReplacement2(self, s: str, k: int) -> int:
        lo, hi = 0, len(s) + 1
        while lo + 1 < hi:
            mid = (lo + hi ) // 2
            if self.isLengthValid(s, k, mid):
                lo = mid
            else:
                hi = mid
        return lo

    """
    일단 한 문자를 볼때 나머지 문자는 무시하는 식으로 생각했다.
    그래서 더 이상 operation을 수행할 수 없을 때까지 윈도우 크기를 계속해서 늘린다
    (lo는 고정 hi는 늘림)
    그리고 수행할 수 없으면 줄인다.
    lo와 hi의 크기 내에 있는 건 항상 valid한 상태를 유지해서 max_length를 업데이트한다
    """
    def characterReplacement1(self, s: str, k: int) -> int:
        characters = set(s)
        max_length = 0
        for character in characters:
            lo, hi = 0, 0
            operation = k
            while hi < len(s):
                if s[hi] != character:
                    if operation > 0:
                        operation -= 1
                    else:
                        while lo < len(s) and s[lo] == character:
                            lo += 1
                        lo += 1
                        if lo == len(s):
                            break
                        if lo > hi:
                            hi = lo
                max_length = max(hi - lo + 1, max_length)
                hi += 1
        return max_length
